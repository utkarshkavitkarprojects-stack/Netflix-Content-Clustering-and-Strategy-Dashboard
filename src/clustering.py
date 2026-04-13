# clustering.py

import pickle


def predict_clusters(X_reduced, artifacts_path="artifacts/"):
    """
    Predict clusters using pre-trained KMeans model.

    Parameters:
        X_reduced (ndarray): SVD-transformed feature matrix
        artifacts_path (str): Path to saved models

    Returns:
        labels (array): Cluster labels
    """

    # Load trained KMeans model
    kmeans = pickle.load(open(artifacts_path + "kmeans_model.pkl", "rb"))

    # Predict clusters
    labels = kmeans.predict(X_reduced)

    return labels