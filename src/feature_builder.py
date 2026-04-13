# feature_builder.py

from scipy.sparse import csr_matrix, hstack


def build_feature_matrix(structured_df, nlp_outputs):
    """
    Combines structured and NLP features into final feature matrix.

    Parameters:
        structured_df (pd.DataFrame): Preprocessed structured data
        nlp_outputs (dict): NLP matrices from process_nlp()

    Returns:
        final_feature_matrix (sparse matrix)
    """

    # -------------------------
    # Convert structured data to sparse matrix
    # -------------------------
    structured_matrix = csr_matrix(structured_df.values)

    # -------------------------
    # Align NLP matrices using index
    # -------------------------
    valid_indices = structured_df.index

    description_matrix = nlp_outputs["description_matrix"][valid_indices]
    title_matrix = nlp_outputs["title_matrix"][valid_indices]
    cast_matrix = nlp_outputs["cast_matrix"][valid_indices]
    director_matrix = nlp_outputs["director_matrix"][valid_indices]

    # -------------------------
    # Combine all matrices
    # -------------------------
    final_feature_matrix = hstack([
        structured_matrix,
        description_matrix,
        title_matrix,
        cast_matrix,
        director_matrix
    ])

    return final_feature_matrix