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
    """

    def __init__(self, n_components : int = None):
        """Default Constructor for Initialization"""

        self.n_components = n_components

    def fit(self, X : np.ndarray):
        """Fit the PCA algorithm into the Dataset"""

        if not self.n_components:
            self.n_components = min(X.shape)