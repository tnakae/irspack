from typing import Iterable as iterable
from typing import Iterator as iterator
from typing import *

from numpy import float32, float64

import irspack.utils._util_cpp

_Shape = Tuple[int, ...]
import scipy.sparse

__all__ = [
    "okapi_BM_25_weight",
    "remove_diagonal",
    "rowwise_train_test_split_d",
    "rowwise_train_test_split_f",
    "rowwise_train_test_split_i",
    "sparse_mm_threaded",
    "tf_idf_weight",
]

def okapi_BM_25_weight(
    X: scipy.sparse.csr_matrix[float64], k1: float = 1.2, b: float = 0.75
) -> scipy.sparse.csr_matrix[float64]:
    pass

def remove_diagonal(
    arg0: scipy.sparse.csr_matrix[float64],
) -> scipy.sparse.csr_matrix[float64]:
    pass

def rowwise_train_test_split_d(
    arg0: scipy.sparse.csr_matrix[float64], arg1: float, arg2: int
) -> Tuple[scipy.sparse.csr_matrix[float64], scipy.sparse.csr_matrix[float64]]:
    pass

def rowwise_train_test_split_f(
    arg0: scipy.sparse.csr_matrix[float32], arg1: float, arg2: int
) -> Tuple[scipy.sparse.csr_matrix[float32], scipy.sparse.csr_matrix[float32]]:
    pass

def rowwise_train_test_split_i(
    arg0: scipy.sparse.csr_matrix[float32], arg1: float, arg2: int
) -> Tuple[scipy.sparse.csr_matrix[float32], scipy.sparse.csr_matrix[float32]]:
    pass

def sparse_mm_threaded(
    arg0: scipy.sparse.csr_matrix[float64],
    arg1: scipy.sparse.csc_matrix[float64],
    arg2: int,
) -> scipy.sparse.csr_matrix[float64]:
    pass

def tf_idf_weight(
    X: scipy.sparse.csr_matrix[float64], smooth: bool = True
) -> scipy.sparse.csr_matrix[float64]:
    pass
