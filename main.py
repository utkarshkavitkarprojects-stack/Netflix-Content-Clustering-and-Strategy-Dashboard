from src.data_loader import load_data
from src.data_preprocessing import preprocess_data
from src.nlp_preprocessing import process_nlp
from src.feature_builder import build_feature_matrix
from src.dimensionality_reduction import apply_svd
from src.clustering import predict_clusters
import pickle


if __name__ == "__main__":

    print("🚀 Starting Netflix Clustering Pipeline...\n")

    # Load data
    df = load_data()
    raw_df = df.copy()

    # NLP
    nlp_outputs = process_nlp(df)

    # Structured preprocessing
    structured_df, mlb, top_countries = preprocess_data(df)

    # Feature building
    final_feature_matrix = build_feature_matrix(structured_df, nlp_outputs)

    # SVD
    X_reduced = apply_svd(final_feature_matrix)

    print(type(X_reduced))
    print(X_reduced.shape)

    # Clustering
    labels = predict_clusters(X_reduced)

    # Assign clusters
    raw_df = raw_df.loc[structured_df.index]
    raw_df['cluster'] = labels

    # Cluster naming
    cluster_map = {
    0: "Modern Streaming-Era Content (Series + Mature Films)",
    1: "Classic & Legacy Cinema",
    2: "Mature & Independent Adult Content (Movies + Series)",
    3: "Mainstream Global Feature Films"
    }

    raw_df['cluster_label'] = raw_df['cluster'].map(cluster_map)

    # Save output
    raw_df.to_csv("artifacts/clustered_netflix_data.csv", index=False)

    # SAVE mlb
    pickle.dump(mlb, open("artifacts/mlb.pkl", "wb"))

    # SAVE top countries
    pickle.dump(top_countries, open("artifacts/top_countries.pkl", "wb"))

    print("\n✅ Pipeline completed successfully!")