from flask import Flask, render_template
import tmdb_client
from flask import request


app = Flask(__name__, template_folder='template')

@app.route('/')
def homepage():

    selected_list = request.args.get('list_type', "popular")

    buttons = [
        {"list_type": "now_playing", "active": "", "display_text": "now playing"},
        {"list_type": "popular", "active": "", "display_text": "popular"},
        {"list_type": "upcoming", "active": "", "display_text": "upcoming"},
        {"list_type": "top_rated", "active": "", "display_text": "top rated"},
    ]

    if selected_list not in ["now_playing", "upcoming", "top_rated"]:
        selected_list = "popular"
    movies = tmdb_client.get_movies(how_many=8, list_type=selected_list)

    for button in buttons:
        if button['list_type'] == selected_list:
            button['active'] = 'active'

    return render_template("homepage.html", movies=movies, current_list=selected_list, buttons=buttons)


@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    details = tmdb_client.get_single_movie(movie_id)
    backdrop_path = details["backdrop_path"]
    base_url_for_backdrop_path = "https://image.tmdb.org/t/p/w500/"
    ready_backdrop_path = f"{base_url_for_backdrop_path}{backdrop_path}"
    cast = tmdb_client.get_single_movie_cast(movie_id)
    return render_template("movie_details.html", movie=details, ready_backdrop_path=ready_backdrop_path, cast=cast)

@app.context_processor
def utility_processor():
    def tmdb_image_url(path):
        return tmdb_client.get_poster_url(path)
    return {"tmdb_image_url": tmdb_image_url}

if __name__ == '__main__':
    app.run(debug=True)
