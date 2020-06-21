from flask import Blueprint, jsonify, request
from . import db
from .model import Movie

main = Blueprint('main', __name__)


@main.route('/add_movie', methods=['POST'])
def add_movie():
    movie_data = request.get_json()
    movie_to_add = Movie(title=movie_data['title'], rating=movie_data['rating'])
    db.session.add(movie_to_add)
    db.session.commit()

    return 'Done', 201


@main.route('/all_movies')
def all_movies():
    all_movies = Movie.query.all()
    movies = []

    for movie in all_movies:
        movies.append({'title': movie.title, 'rating': movie.rating})
    return jsonify({'movies': movies})
