import os
import datetime
import psycopg2
from dotenv import load_dotenv

load_dotenv()

connection = psycopg2.connect(os.environ["DATABASE_URL"])

# SQL COMMANDS

CREATE_MOVIES_TABLE = """
create table if not exists movies (
    movie_id SERIAL PRIMARY KEY,
    title TEXT,
    release_timestamp REAL);"""

CREATE_USERS_TABLE = """
create table if not exists users (
    user_id SERIAL PRIMARY KEY,
    name TEXT);"""

CREATE_WATCHED_TABLE = """
create table if not exists watched (
    movie_id INTEGER,
    user_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (movie_id) REFERENCES movies(movie_id));"""

INSERT_USER = """
insert into users (name) values (%s);"""

INSERT_MOVIE = """
insert into movies (title, release_timestamp) values (%s,%s);"""

INSERT_WATCHED_MOVIE = """
insert into watched (movie_id, user_id) values (%s,%s);"""

DELETE_MOVIE = """
delete from movies where movie_id = %s;"""

SELECT_ALL_MOVIES = """
select movie_id, title, release_timestamp from movies;"""

SELECT_UPCOMING_MOVIES = """
select movie_id, title, release_timestamp from movies where release_timestamp > %s;"""

SELECT_WATCHED_MOVIES = """
select m.title from watched w inner join movies m on w.movie_id = m.movie_id inner join users u on w.user_id = u.user_id where u.name = %s;"""

SELECT_USERS = """
select user_id, name from users;"""

RESET_TABLES = """
delete from watched; delete from movies; delete from users;
"""

# SQL METHODS

def create_tables():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_MOVIES_TABLE)
            cursor.execute(CREATE_USERS_TABLE)
            cursor.execute(CREATE_WATCHED_TABLE)

def add_user(name):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(INSERT_USER, (name,))

def add_movie(title, release_timestamp):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(INSERT_MOVIE, (title, release_timestamp))

def get_movies(upcoming=False):
    with connection:
        with connection.cursor() as cursor:
            if upcoming:
                today_timestamp = datetime.datetime.today().timestamp()
                cursor.execute(SELECT_UPCOMING_MOVIES, (today_timestamp,))
            else:
                cursor.execute(SELECT_ALL_MOVIES)
            return cursor.fetchall()

def watch_movie(user_id, movie_id):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(INSERT_WATCHED_MOVIE, (user_id, movie_id))

def get_watched_movies(watcher_name):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(SELECT_WATCHED_MOVIES, (watcher_name,))
            return cursor.fetchall()

def get_users():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(SELECT_USERS)
            return cursor.fetchall()

def reset_tables():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(RESET_TABLES)

