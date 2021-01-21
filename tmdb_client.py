from flask import *
import requests


"""Zwróć uwagę, że dodaliśmy tutaj jeszcze linię response.raise_for_status(). 
Jej obecność spowoduje, że jeśli odpowiedź od API zakończy się czymkolwiek innym niż sukcesem 
aplikacja zwróci wyjątek. Dzięki temu możemy mieć pewność, 
że operujemy tylko i wyłącznie na poprawnych danych pobranych z API."""


def call_tmdb_api(endpoint):

    base_url = f"https://api.themoviedb.org/3/{endpoint}"
    api_key = "?api_key=b8f3773bcd06b8216b858401bd1c6efa"
    response = requests.get(f"{base_url}{api_key}")
    response.raise_for_status()
    return response.json()


def get_movies_list(list_type="popular"):
    return call_tmdb_api(f"movie/{list_type}")

# Glowny obraz filmu

# 2 z 3


def get_poster_url(poster_api_path):
    base_url = "https://image.tmdb.org/t/p/w342/"
    return f"{base_url}/{poster_api_path}"


def get_movies(how_many, list_type):
    data = get_movies_list(list_type)
    return data["results"][:how_many]

# 1 z 3

"""Stwórz testy jednostkowe dla Twojej biblioteki filmów. 
Przetestuj funkcje takie jak get_single_movie, 
get_movie_images, get_single_movie_cast."""
# czy to wogole warto sprawdzac w test_tmdb?
# ta funkcja tylko przyjmuje movie_id i zwraca to do call_tmdb_api a ta funkcja jest juz przetestowana

def get_single_movie(movie_id):
    return call_tmdb_api(f"movie/{movie_id}")

# 3 z3


def get_single_movie_cast(movie_id):
    base_url = "https://api.themoviedb.org/3/movie/"
    cast = "/credits"
    api_key = "?api_key=b8f3773bcd06b8216b858401bd1c6efa"
    ready = requests.get(f"{base_url}{movie_id}{cast}{api_key}")
    return ready.json()["cast"]
