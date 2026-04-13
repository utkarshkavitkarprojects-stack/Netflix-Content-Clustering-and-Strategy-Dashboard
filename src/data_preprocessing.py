# preprocessing.py

import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer


def preprocess_data(df):
    """
    Preprocess structured Netflix dataset.

    Returns:
        pd.DataFrame
    """

    df = df.copy()

    # -------------------------
    # Remove duplicates
    # -------------------------
    df = df.drop_duplicates()

    # -------------------------
    # Date processing
    # -------------------------
    df['date_added'] = df['date_added'].str.strip()
    df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

    df['year_added'] = df['date_added'].dt.year
    df['month_added'] = df['date_added'].dt.month

    # Drop rows where date is critical
    df = df.dropna(subset=['date_added', 'year_added', 'month_added'])

    df = df.drop('date_added', axis=1)

    # -------------------------
    # Missing values
    # -------------------------
    df['country'] = df['country'].fillna('Unknown')
    df['rating'] = df['rating'].fillna('Not Rated')

    # -------------------------
    # Drop unnecessary columns
    # -------------------------
    df = df.drop(['type', 'duration', 'description', 'title', 'cast', 'director'], axis=1)

    # -------------------------
    # Genre processing
    # -------------------------
    df['listed_in'] = df['listed_in'].apply(lambda x: x.split(','))

    mlb = MultiLabelBinarizer()

    genre_df = pd.DataFrame(
        mlb.fit_transform(df['listed_in']),
        columns=mlb.classes_,
        index=df.index
    )

    df = pd.concat([df, genre_df], axis=1)
    df = df.drop('listed_in', axis=1)

    # -------------------------
    # Country reduction
    # -------------------------
    top_countries = df['country'].value_counts().head(15).index

    df['country'] = df['country'].apply(
        lambda x: x if x in top_countries else 'Other'
    )

    # -------------------------
    # Encoding
    # -------------------------
    df = pd.get_dummies(df, columns=['country', 'rating'], drop_first=True)

    # -------------------------
    # Clean columns
    # -------------------------
    df.columns = df.columns.str.strip()
    df = df.loc[:, ~df.columns.duplicated()]

    # -------------------------
    # Convert to numeric
    # -------------------------
    df = df.apply(pd.to_numeric, errors='coerce')
    df = df.fillna(0)
    df = df.astype(int)

    return df