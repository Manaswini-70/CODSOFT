import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies = {
    "title": [
        "The Matrix",
        "The Godfather",
        "The Dark Knight",
        "Pulp Fiction",
        "Inception",
        "Fight Club",
        "Forrest Gump"
    ],
    "genre": [
        "Action Sci-Fi",
        "Crime Drama",
        "Action Crime Drama",
        "Crime Drama",
        "Action Sci-Fi Thriller",
        "Drama Thriller",
        "Drama Romance"
    ]
}

df = pd.DataFrame(movies)
vectorizer = TfidfVectorizer(stop_words="english")
genre_matrix = vectorizer.fit_transform(df["genre"])
similarity = cosine_similarity(genre_matrix)

def recommend(movie_title, num_recommendations=3):
    if movie_title not in df["title"].values:
        return f"Movie '{movie_title}' not found in dataset."
    idx = df[df["title"] == movie_title].index[0]
    sim_scores = list(enumerate(similarity[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:num_recommendations+1]
    recommended = [df.iloc[i[0]]["title"] for i in sim_scores]
    return recommended

print("Movie Recommendation System")
movie_name = input("Enter a movie name: ")
results = recommend(movie_name)

print("\nRecommended Movies:")
if isinstance(results, list):
    for r in results:
        print(r)
else:
    print(results)
