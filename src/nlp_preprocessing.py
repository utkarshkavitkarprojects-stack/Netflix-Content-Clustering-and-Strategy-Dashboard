# nlp_preprocessing.py

import re
import pandas as pd
import nltk
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
import pickle


# Initialize NLP tools
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()


# -------------------------
# Helper Functions
# -------------------------

def fix_mojibake(text):
    try:
        return text.encode('latin1').decode('utf-8')
    except:
        return text


def preprocess_description(text):
    text = text.lower()
    text = re.sub(r'<.*?>', ' ', text)
    text = re.sub(r'http\S+|www\S+', ' ', text)
    text = re.sub(r'[^a-zA-Z\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()

    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in stop_words and len(word) > 2]
    tokens = [lemmatizer.lemmatize(word) for word in tokens]

    return ' '.join(tokens)


def preprocess_title(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def preprocess_director(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z,\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    text = text.replace(',', ' ')
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def preprocess_cast(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z,\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    text = text.replace(',', ' ')
    text = re.sub(r'\s+', ' ', text).strip()
    return text


# -------------------------
# Main NLP Pipeline
# -------------------------

def process_nlp(df, artifacts_path="artifacts/"):

    text_df = df[['title', 'director', 'cast', 'description']].copy()
    text_df = text_df.fillna('')

    for col in text_df.columns:
        text_df[col] = text_df[col].apply(fix_mojibake)

    text_df['description_clean'] = text_df['description'].apply(preprocess_description)
    text_df['title_clean'] = text_df['title'].apply(preprocess_title)
    text_df['director_clean'] = text_df['director'].apply(preprocess_director)
    text_df['cast_clean'] = text_df['cast'].apply(preprocess_cast)

    # -------------------------
    # Load vectorizers
    # -------------------------
    description_vectorizer = pickle.load(open(artifacts_path + "desc_vectorizer.pkl", "rb"))
    title_vectorizer = pickle.load(open(artifacts_path + "title_vectorizer.pkl", "rb"))
    cast_vectorizer = pickle.load(open(artifacts_path + "cast_vectorizer.pkl", "rb"))
    director_vectorizer = pickle.load(open(artifacts_path + "director_vectorizer.pkl", "rb"))

    # -------------------------
    # Transform only
    # -------------------------
    description_matrix = description_vectorizer.transform(text_df['description_clean'])
    title_matrix = title_vectorizer.transform(text_df['title_clean'])
    cast_matrix = cast_vectorizer.transform(text_df['cast_clean'])
    director_matrix = director_vectorizer.transform(text_df['director_clean'])

    return {
        "description_matrix": description_matrix,
        "title_matrix": title_matrix,
        "cast_matrix": cast_matrix,
        "director_matrix": director_matrix
    }