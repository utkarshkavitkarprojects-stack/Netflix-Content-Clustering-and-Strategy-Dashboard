# 🎬 Netflix Content Clustering & Strategy Analysis

## 🚀 Project Overview

This project applies **Unsupervised Machine Learning (K-Means Clustering)** to segment Netflix content into meaningful groups based on both **structured metadata** and **textual features**.

The goal is to uncover **hidden content patterns** and translate them into **business insights** that can help Netflix improve:

* Content strategy
* Audience targeting
* Recommendation systems
* Content acquisition decisions

---

## 📊 Problem Statement

Netflix hosts a vast and diverse content library. However, without structured segmentation, it becomes difficult to:

* Understand content distribution
* Identify audience segments
* Optimize content investments

👉 This project solves that by clustering content into **interpretable business segments**.

---

## 🌐 Live Demo

🚀 Try the deployed app here:
👉 https://netflix-content-clustering-and-strategy-dashboard.streamlit.app/

⚠️ Note: The app may take a few seconds to load initially due to inactivity (free hosting behavior).

---

## 🧠 Approach

### 1. Data Processing

* Cleaned dataset and handled missing values
* Extracted:

  * `year_added`, `month_added`
* Encoded:

  * Genres using **MultiLabelBinarizer**
  * Country & Rating using **One-Hot Encoding**

---

### 2. NLP Feature Engineering

Applied preprocessing on:

* Title
* Cast
* Director
* Description

Techniques used:

* Lowercasing & cleaning
* Stopword removal
* Lemmatization
* TF-IDF Vectorization (for text importance)
* Count Vectorization (for entities like cast & director)

---

### 3. Feature Engineering

* Combined structured + NLP features into a single matrix
* Used **sparse matrix stacking** for efficiency

---

### 4. Dimensionality Reduction

* Applied **Truncated SVD (100 components)**
  👉 Reduced dimensionality while preserving semantic structure

---

### 5. Clustering

* Model: **K-Means**
* Final clusters selected: **k = 4**

---

## 🎯 Final Clusters & Interpretation

### 🔹 Cluster 0 — Modern Streaming-Era Content

* Recent (2016–2018)
* Strong presence of:

  * TV Shows
  * TV-MA rating
  * International content

👉 **Insight:**
Represents Netflix’s core streaming strategy — binge-worthy, global, mature content.

---

### 🔹 Cluster 1 — Classic & Legacy Cinema

* Older content (~1970s–2000)
* Dominated by:

  * Classic Movies
  * Drama, Action

👉 **Insight:**
Archival content serving nostalgia-driven audiences.

---

### 🔹 Cluster 2 — Mature & Independent Adult Content

* Recent (~2016)
* Strong signals:

  * Independent Movies
  * TV-MA
  * Drama-heavy

👉 **Insight:**
Niche, high-depth storytelling content for mature audiences.

---

### 🔹 Cluster 3 — Mainstream Global Feature Films

* Mid-era (~2000–2010)
* Balanced genres:

  * Action, Romance, Comedy

👉 **Insight:**
Broad appeal commercial cinema targeting mass audiences globally.

---

## 📈 Key Business Insights

### 1. Netflix’s Core Strength = Modern Streaming Content

* Cluster 0 dominates recent additions
* Strong presence of:

  * Series
  * Mature content
  * International shows

👉 **Recommendation:**
Continue investing heavily in **original series + global storytelling**

---

### 2. Clear Audience Segmentation Exists

Clusters naturally map to audience types:

| Cluster          | Audience Type     |
| ---------------- | ----------------- |
| Modern Streaming | Binge watchers    |
| Classic Cinema   | Nostalgia viewers |
| Indie/Mature     | Niche audiences   |
| Mainstream Films | Mass market       |

👉 **Recommendation:**
Improve personalization using **cluster-based recommendations**

---

### 3. Growth Opportunity in Independent Content

* Cluster 2 shows strong niche demand

👉 **Recommendation:**
Expand investment in:

* Indie films
* Dark storytelling
* Festival-type content

---

### 4. Global Content is a Major Driver

* High presence of **International Movies & TV Shows**

👉 **Recommendation:**
Focus on:

* Regional content (India, Korea, Spain)
* Localization strategies

---

### 5. Balanced Portfolio Strategy

Netflix content falls into:

* Evergreen classics
* Modern originals
* Commercial films
* Niche indie

👉 **Recommendation:**
Maintain **portfolio diversification** to retain all audience segments

---

## 📊 Streamlit Dashboard

An interactive dashboard was built to:

* Explore clusters
* Filter content
* Analyze genres, countries, ratings
* Download filtered datasets

### Features:

* 🎯 Cluster-based filtering
* 🔍 Search functionality
* 📊 Visual insights
* 📥 CSV download

---

## 🛠️ Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* NLTK
* Streamlit
* SciPy (sparse matrices)

---

## 📁 Project Structure

```
├── artifacts/
│   ├── cast_vectorizer.pkl
│   ├── clustered_netflix_data.csv
│   ├── desc_vectorizer.pkl 
│   ├── director_vectorizer.pkl
│   ├── kmeans_model.pkl
│   ├── svd_model.pkl
│   ├── title_vectorizer.pkl
│
├── assets/
│   ├── app_home.png
│   ├── insights.png
│   ├── Explore_data.png
│   
├── data/raw 
│   ├── NETFLIX MOVIES AND TV SHOWS CLUSTERING
│
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_text_preprocessing.ipynb
│   ├── 03_data_preprocessing.ipynb
│   ├── 04_model_experiments.ipynb
│   ├── 05_final_model.ipynb
│   ├── 06_business_insights.ipynb
│   ├── Netflix_Clustering_main.ipynb
|
├── src/
│   ├── data_loader.py
│   ├── data_preprocessing.py
│   ├── nlp_preprocessing.py
│   ├── feature_builder.py
│   ├── dimensionality_reduction.py
│   ├── clustering.py
│
├── app.py
├── .gitignore
├── main.py
├── requirements.txt
└── README.md
```

---

## 🎯 Key Learnings

* Combining **NLP + structured data** improves clustering quality
* Dimensionality reduction is critical for high-dimensional sparse data
* Unsupervised learning can generate **actionable business insights**
* Building **end-to-end pipelines + UI** is crucial for real-world ML

---

## 🚀 Future Improvements

* Add **real-time clustering for new content**
* Integrate with recommendation engine
* Add similarity search (content recommendation)

---

## 👤 Author

**Utkarsh Kavitkar**
Aspiring Data Scientist | Machine Learning Enthusiast

---

## ⭐ Final Note

This project demonstrates:

* End-to-end ML pipeline
* Real-world problem solving
* Business-oriented thinking
* Product-level deployment

👉 Not just a model — but a **complete data science solution**
