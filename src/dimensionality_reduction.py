# dimensionality_reduction.py

from sklearn.decomposition import TruncatedSVD
import pickle

def apply_svd(feature_matrix, artifacts_path="artifacts/"):
    """
    Applies Truncated SVD for dimensionality reduction.

    Parameters:
        feature_matrix (sparse matrix): Combined feature matrix
        n_components (int): Number of components
        random_state (int): Random seed

    Returns:
        X_reduced (ndarray): Reduced feature matrix
        svd_model (TruncatedSVD): Fitted SVD model
    """

    svd = pickle.load(open(artifacts_path + "svd_model.pkl", "rb"))
    X_reduced = svd.fit_transform(feature_matrix)

    return X_reduced