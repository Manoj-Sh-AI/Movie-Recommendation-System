import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=b0fe7a443821816aa3fe051e3cc8fd44&language=en-US".format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data["poster_path"]

# FINAL RECOMENDATION ALGORITHM
def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recomended_movies_posters = []
    # printing the list of movies
    for i in movies_list:
        movie_id = movies.iloc[i[0]].id
        # fetch poster
        recommended_movies.append(movies.iloc[i[0]].title)  # prints the title of the movie
        recomended_movies_posters.append(fetch_poster(movie_id))
        # print(i[0]) -> prints the index of the recomended movie
    return recommended_movies, recomended_movies_posters


movies_dict = pickle.load(open("movies_dict.pkl", "rb"))   # we are opening the file using read binary mode
movies = pd.DataFrame(movies_dict)  # gives the names of the movies

similarity = pickle.load(open("similarity.pkl", "rb"))

st.title("Movie Recommender System")

selected_movie_name = st.selectbox('How would you like to be contacted?', movies["title"].values)  # the movies title will be fetched in the dropdown


if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])
