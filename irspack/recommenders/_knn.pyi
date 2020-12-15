import irspack.recommenders._knn
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import scipy.sparse
__all__  = [
"AsymmetricSimilarityComputer",
"CosineSimilarityComputer",
"JaccardSimilarityComputer",
"P3alphaComputer"
]
class AsymmetricSimilarityComputer():
    def __init__(self, X: scipy.sparse.csr_matrix[float64], shrinkage: float, alpha: float, n_thread: int) -> None: ...
    def compute_similarity(self, arg0: scipy.sparse.csr_matrix[float64], arg1: int) -> scipy.sparse.csr_matrix[float64]: ...
    pass
class CosineSimilarityComputer():
    def __init__(self, X: scipy.sparse.csr_matrix[float64], shrinkage: float, normalize: bool, n_thread: int = 1) -> None: ...
    def compute_similarity(self, arg0: scipy.sparse.csr_matrix[float64], arg1: int) -> scipy.sparse.csr_matrix[float64]: ...
    pass
class JaccardSimilarityComputer():
    def __init__(self, X: scipy.sparse.csr_matrix[float64], shrinkage: float, n_thread: int = 1) -> None: ...
    def compute_similarity(self, arg0: scipy.sparse.csr_matrix[float64], arg1: int) -> scipy.sparse.csr_matrix[float64]: ...
    pass
class P3alphaComputer():
    def __init__(self, X: scipy.sparse.csr_matrix[float64], alpha: float, normalize: bool, n_thread: int) -> None: ...
    def compute_similarity(self, arg0: scipy.sparse.csr_matrix[float64], arg1: int) -> scipy.sparse.csr_matrix[float64]: ...
    pass
