# -*- encoding: utf-8 -*-

import numpy as np

class PCA(object):
    """Dimension Reduction using Principal Component Analysis (PCA)

    It is the procces of computing principal components which explains the
    maximum variation of the dataset using fewer components.

    :type  n_components: int, optional
    :param n_components: Number of components to consider, if not set then
                         `n_components = min(n_samples, n_features)`, where
                         `n_samples` is the number of samples, and
                         `n_features` is the number of features (i.e.,
                         dimension of the dataset).

    :Attributes:
    :type  covariance_: np.ndarray
    :param covariance_: Coviarance Matrix

    :type  eig_vals_: np.ndarray
    :param eig_vals_: Calculated Eigen Values

    :type  eig_vecs_: np.ndarray
    :param eig_vecs_: Calculated Eigen Vectors

    :type  explained_variance_: np.ndarray
    :param explained_variance_: Explained Variance of Each Principal Components

    :type  cum_explained_variance_: np.ndarray
    :param cum_explained_variance_: Cumulative Explained Variables
    """

    def __init__(self, n_components : int = None):
        """Default Constructor for Initialization"""

        self.n_components = n_components

    def fit_transform(self, X : np.ndarray):
        """Fit the PCA algorithm into the Dataset"""

        if not self.n_components:
            self.n_components = min(X.shape)

        self.covariance_ = np.cov(X.T)

        # calculate eigens
        self.eig_vals_, self.eig_vecs_ = np.linalg.eig(self.covariance_)
        # self.eig_pairs_ = [(np.abs(self.eig_vals_[i]), self.eig_vecs_[:, i]) for i in range(len(self.eig_vals_))]

        # explained variance
        _tot_eig_vals = sum(self.eig_vals_)
        self.explained_variance_ = np.array([(i / _tot_eig_vals) * 100 for i in sorted(self.eig_vals_, reverse = True)])
        self.cum_explained_variance_ = np.cumsum(self.explained_variance_)

        # define `W` as `d x k`-dimension
        self.W_ = self.eig_vecs_[:, :self.n_components]

        print(X.shape, self.W_.shape)
        return X.dot(self.W_)
