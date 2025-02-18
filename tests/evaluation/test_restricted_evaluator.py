from collections import defaultdict
from typing import Any, List

import numpy as np
import pytest
from scipy import sparse as sps

from irspack.evaluation import Evaluator
from irspack.recommenders.base import BaseRecommender


class MockRecommender(BaseRecommender, register_class=False):
    def __init__(self, X_all: sps.csr_matrix, scores: np.ndarray) -> None:
        super().__init__(X_all)
        self.scores = scores

    def get_score(self, user_indices: np.ndarray) -> np.ndarray:
        return self.scores[user_indices]

    def _learn(self) -> None:
        pass


@pytest.mark.parametrize("U, I, R", [(10, 30, 10), (100, 30, 5), (30, 100, 2)])
def test_restriction_global(U: int, I: int, R: int) -> None:
    try:
        from sklearn.metrics import ndcg_score
    except:
        pytest.skip()
    rns = np.random.RandomState(42)
    recommendable = rns.choice(np.arange(I), replace=False, size=R)
    scores = rns.randn(U, I)
    X_gt = (rns.rand(U, I) >= 0.3).astype(np.float64)
    evaluator_ = Evaluator(
        sps.csr_matrix(X_gt),
        offset=0,
        cutoff=I,
        n_threads=1,
        recommendable_items=recommendable,
    )
    # empty mask
    mock_rec = MockRecommender(sps.csr_matrix(X_gt.shape), scores)
    my_score = evaluator_.get_score(mock_rec)
    sklearn_metrics = defaultdict(list)
    for i in range(scores.shape[0]):
        if X_gt[i, recommendable].sum() == 0:
            continue
        ndcg = ndcg_score(
            X_gt[i, recommendable][None, :], scores[i, recommendable][None, :]
        )
        sklearn_metrics["ndcg"].append(ndcg)

    assert my_score["ndcg"] == pytest.approx(np.mean(sklearn_metrics["ndcg"]), abs=1e-8)


@pytest.mark.parametrize(
    "U, I, is_sparse", [(10, 30, False), (100, 30, True), (30, 100, False)]
)
def test_restriction_local(U: int, I: int, is_sparse: bool) -> None:
    try:
        from sklearn.metrics import ndcg_score
    except:
        pytest.skip()
    rns = np.random.RandomState(42)
    recommendables: List[List[int]] = []

    def _to_int_list(x: Any) -> List[int]:
        return [int(_) for _ in x]

    for _ in range(U):
        recommendables.append(
            _to_int_list(
                rns.choice(np.arange(I), replace=False, size=rns.randint(2, I))
            )
        )
    if is_sparse:
        indices = [j for r in recommendables for j in sorted(r)]
        indptr = np.cumsum([0] + [len(r) for r in recommendables])
        recommendables_arg = sps.csr_matrix(
            (np.ones(len(indices), dtype=float), indices, indptr), shape=(U, I)
        )
    else:
        recommendables_arg = recommendables
    scores = rns.randn(U, I)
    X_gt = (rns.rand(U, I) >= 0.3).astype(np.float64)
    eval = Evaluator(
        sps.csr_matrix(X_gt),
        offset=0,
        cutoff=I,
        n_threads=1,
        per_user_recommendable_items=recommendables_arg,
    )
    # empty mask
    mock_rec = MockRecommender(sps.csr_matrix(X_gt.shape), scores)
    my_score = eval.get_score(mock_rec)
    sklearn_metrics = defaultdict(list)
    for i in range(scores.shape[0]):
        if X_gt[i, recommendables[i]].sum() == 0:
            continue
        ndcg = ndcg_score(
            X_gt[i, recommendables[i]][None, :], scores[i, recommendables[i]][None, :]
        )
        sklearn_metrics["ndcg"].append(ndcg)

    assert my_score["ndcg"] == pytest.approx(np.mean(sklearn_metrics["ndcg"]), abs=1e-8)


@pytest.mark.parametrize("U, I", [(10, 30)])
def test_irregular(U: int, I: int) -> None:
    rns = np.random.RandomState(42)
    recommendables: List[np.ndarray] = []
    X_gt = (rns.rand(U, I) >= 0.3).astype(np.float64)
    _ = Evaluator(
        sps.csr_matrix(X_gt),
        offset=0,
        cutoff=I,
        n_threads=1,
        per_user_recommendable_items=[[0] for _ in range(X_gt.shape[0])],
    )
    _ = Evaluator(
        sps.csr_matrix(X_gt),
        offset=0,
        cutoff=I,
        n_threads=1,
        per_user_recommendable_items=sps.csr_matrix(X_gt),
    )

    with pytest.raises(ValueError):
        _ = Evaluator(
            sps.csr_matrix(X_gt),
            offset=0,
            cutoff=I,
            n_threads=1,
            per_user_recommendable_items=[[0], [0]],
        )
    with pytest.raises(ValueError):
        _ = Evaluator(
            sps.csr_matrix(X_gt),
            offset=0,
            cutoff=I,
            n_threads=1,
            per_user_recommendable_items=[[0, 0]],
        )
    with pytest.raises(ValueError):
        _ = Evaluator(
            sps.csr_matrix(X_gt),
            offset=0,
            cutoff=I,
            n_threads=1,
            per_user_recommendable_items=[
                [
                    I,
                ]
            ],
        )
    with pytest.raises(ValueError):
        _ = Evaluator(
            sps.csr_matrix(X_gt),
            offset=0,
            cutoff=I,
            n_threads=1,
            per_user_recommendable_items=X_gt[:-1],
        )
