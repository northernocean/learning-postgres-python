import sqlite3
import datetime

connection = sqlite3.connect("data.db")

# SQL COMMANDS

CREATE_MOVIES_TABLE = """
create table if not exists movies (
    id INTEGER PRIMARY KEY,
    title TEXT,
    release_timestamp REAL);"""

CREATE_USERS_TABLE = """
create table if not exists users (
    id INTEGER PRIMARY KEY,
    name TEXT);"""

CREATE_WATCHED_TABLE = """
create table if not exists watched (
    movie_id INTEGER,
    user_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (movie_id) REFERENCES movies(id));"""

INSERT_USER = """
insert into users (name) values (?);"""

INSERT_MOVIE = """
insert into movies (title, release_timestamp) values (?,?);"""

INSERT_WATCHED_MOVIE = """
insert into watched (movie_id, user_id) values (?,?);"""

DELETE_MOVIE = """
delete from movies where id = ?;"""

SELECT_ALL_MOVIES = """
select id, title, release_timestamp from movies;"""

SELECT_UPCOMING_MOVIES = """
select id, title, release_timestamp from movies where release_timestamp > ?;"""

SELECT_WATCHED_MOVIES = """
select m.title from watched w inner join movies m on w.movie_id = m.id inner join users u on w.user_id = u.id where u.name = ?;"""

SELECT_USERS = """
select id, name from users;"""

# SQL METHODS

def create_tables():
    with connection:
        connection.execute(CREATE_MOVIES_TABLE)
        connection.execute(CREATE_USERS_TABLE)
        connection.execute(CREATE_WATCHED_TABLE)

def add_user(name):
    with connection:
        connection.execute(INSERT_USER, (name,))

def add_movie(title, release_timestamp):
    with connection:
        connection.execute(INSERT_MOVIE, (title, release_timestamp))

def get_movies(upcoming=False):
    with connection:
        cursor = connection.cursor()
        if upcoming:
            today_timestamp = datetime.datetime.today().timestamp()
            cursor.execute(SELECT_UPCOMING_MOVIES, (today_timestamp,))
        else:
            cursor.execute(SELECT_ALL_MOVIES)
        return cursor.fetchall()

def watch_movie(user_id, movie_id):
    with connection:
        connection.execute(INSERT_WATCHED_MOVIE, (user_id, movie_id))

def get_watched_movies(watcher_name):
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_WATCHED_MOVIES, (watcher_name,))
        return cursor.fetchall()

def get_users():
    with connection:
        return connection.execute(SELECT_USERS).fetchall()