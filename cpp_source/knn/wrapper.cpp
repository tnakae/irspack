#include "knn.hpp"
#include "similarities.hpp"
#include <Eigen/Sparse>
#include <cstddef>
#include <pybind11/eigen.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <stdexcept>

namespace py = pybind11;
using Real = double;

PYBIND11_MODULE(_knn, m) {
  py::class_<KNN::CosineSimilarityComputer<Real>>(m, "CosineSimilarityComputer")
      .def(py::init<const KNN::CosineSimilarityComputer<Real>::CSRMatrix &,
                    Real, bool, size_t>(),
           py::arg("X"), py::arg("shrinkage"), py::arg("normalize"),
           py::arg("n_thread") = 1)
      .def("compute_similarity",
           &KNN::CosineSimilarityComputer<Real>::compute_similarity);

  py::class_<KNN::JaccardSimilarityComputer<Real>>(m,
                                                   "JaccardSimilarityComputer")
      .def(py::init<const KNN::JaccardSimilarityComputer<Real>::CSRMatrix &,
                    Real, size_t>(),
           py::arg("X"), py::arg("shrinkage"), py::arg("n_thread") = 1)
      .def("compute_similarity",
           &KNN::JaccardSimilarityComputer<Real>::compute_similarity);

  py::class_<KNN::AsymmetricCosineSimilarityComputer<Real>>(
      m, "AsymmetricSimilarityComputer")
      .def(py::init<
               const KNN::AsymmetricCosineSimilarityComputer<Real>::CSRMatrix &,
               Real, Real, size_t>(),
           py::arg("X"), py::arg("shrinkage"), py::arg("alpha"),
           py::arg("n_thread"))
      .def("compute_similarity",
           &KNN::AsymmetricCosineSimilarityComputer<Real>::compute_similarity);

  py::class_<KNN::P3alphaComputer<Real>>(m, "P3alphaComputer")
      .def(py::init<const KNN::P3alphaComputer<Real>::CSRMatrix &, Real, bool,
                    size_t>(),
           py::arg("X"), py::arg("alpha") = 0, py::arg("normalize") = false,
           py::arg("n_thread"))
      .def("compute_W", &KNN::P3alphaComputer<Real>::compute_W);
}