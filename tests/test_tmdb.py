from flask import *
import requests
import tmdb_client
from unittest.mock import Mock


def test_get_movies_list(monkeypatch):
    # Lista, którą będzie zwracać przysłonięte "zapytanie do API"
    mock_movies_list = ['Movie 1', 'Movie 2']

    requests_mock = Mock()
    # Wynik wywołania zapytania do API
    #response = requests_mock.return_value
    # Przysłaniamy wynik wywołania metody .json()
    #response.json.return_value = mock_movies_list

    requests_mock.return_value.json.return_value = ['Movie 1', 'Movie 2']

    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

    movies_list = tmdb_client.get_movies_list(list_type="popular")
    assert movies_list == mock_movies_list


def test_get_single_movie(monkeypatch):
    mock_single_movie = "111111"
    requests_mock = Mock()
    requests_mock.json.return_value = mock_single_movie
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)
    single_movie = tmdb_client.get_single_movie(movie_id="508442")
    return single_movie == mock_single_movie


def test_get_poster_url(monkeypatch):
    mock_poster_url = "https://image.tmdb.org/t/p/w342/kIHgjAkuzvKBnmdstpBOo4AfZah"
    requests_mock = Mock()
    requests_mock.json.return_value = mock_poster_url
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)
    single_poster_url = tmdb_client.get_poster_url(poster_api_path="8UlWHLMpgZm9bx6QYh0NFoq67TZ")
    return single_poster_url == mock_poster_url


def test_get_single_movie_cast(monkeypatch):
    mock_cast = "Robert P"
    mock_single_movie = {"cast": mock_cast}
    requests_mock = Mock()
    requests_mock.return_value.json.return_value = mock_single_movie
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)
    
    single_movie_cast = tmdb_client.get_single_movie_cast(movie_id="696374")
    return single_movie_cast == mock_single_movie


