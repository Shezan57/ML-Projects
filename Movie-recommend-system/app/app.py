import streamlit as st
import pandas as pd
import numpy as np
import pickle
import requests
import os

# Load the dataset
movies_list = pickle.loads(open('../movies_dict.pkl', 'rb').read())
movies = pd.DataFrame(movies_list)
similarity = pickle.loads(open('../similarity.pkl', 'rb').read())


def fetch_poster(movie_id):
    url = 'https://api.themoviedb.org/3/movie/{}?api_key=507b9bbb1f0366f81f7c303f7a24aeb3&language=en-US'.format(movie_id)
    data = requests.get(url)
    data = data.json()
    print(data)
    poster_path = data['poster_path']
    full_path = 'https://image.tmdb.org/t/p/w500/' + poster_path
    return full_path
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list1 = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list1:
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters


st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Which movie do you like?',
    movies['title'].values)

if st.button('Recommend'):
    recommendations, posters = recommend(selected_movie_name)
    # for i in range(len(recommendations)):
    #     st.write(f'{i + 1}. {recommendations[i]}')
    st.write('Top 5 Recommendations for you:')
    col1, col2, col3, col4, col5 = st.columns(5)  # , col6, col7, col8, col9, col10
    with col1:
        st.text(recommendations[0])
        st.image(posters[0])

    with col2:
        st.text(recommendations[1])
        st.image(posters[1])

    with col3:
        st.text(recommendations[2])
        st.image(posters[2])

    with col4:
        st.text(recommendations[3])
        st.image(posters[3])

    with col5:
        st.text(recommendations[4])
        st.image(posters[4])

    # with col6:
    #     st.text(recommendations[5])
    #     st.image(posters[5])
    # with col7:
    #     st.text(recommendations[6])
    #     st.image(posters[6])
    # with col8:
    #     st.text(recommendations[7])
    #     st.image(posters[7])
    # with col9:
    #     st.text(recommendations[8])
    #     st.image(posters[8])
    # with col10:
    #     st.text(recommendations[9])
    #     st.image(posters[9])

