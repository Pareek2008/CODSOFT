# Task 3: Smart Recommendation System using TF-IDF & Cosine Similarity

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample dataset (can be replaced with CSV)
data = {
    'Title': [
        'Machine Learning Basics',
        'Deep Learning with Python',
        'Data Science Handbook',
        'Intro to Artificial Intelligence',
        'Python Crash Course',
        'AI for Everyone',
        'Natural Language Processing Guide',
        'Advanced Python Tricks',
        'AI in Healthcare',
        'Data Analysis with Pandas'
    ],
    'Description': [
        'Introduction to Machine Learning concepts and algorithms',
        'Deep learning techniques using TensorFlow and Keras',
        'Essential guide to data science methods and tools',
        'Basics of artificial intelligence and machine perception',
        'Beginner-friendly Python programming course',
        'Understanding AI impact and its real-world uses',
        'Guide to processing and analyzing human language',
        'Advanced tips for writing clean Python code',
        'Applications of AI in healthcare and diagnostics',
        'Data cleaning, analysis, and visualization using pandas'
    ]
}

df = pd.DataFrame(data)

# Vectorize descriptions
tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(df['Description'])

def recommend(query, top_n=3):
    query_vec = tfidf.transform([query])
    similarity = cosine_similarity(query_vec, tfidf_matrix).flatten()
    indices = similarity.argsort()[::-1][:top_n]

    print(f"\n📊 Top {top_n} recommendations for: \"{query}\"\n")
    for idx in indices:
        print(f"✅ {df.iloc[idx]['Title']} — {df.iloc[idx]['Description']}")

print("🔎 Welcome to Smart Recommendation System!")
user_input = input("💬 What are you interested in? (e.g., AI, NLP, Python, Healthcare)\nYou: ")
recommend(user_input)
