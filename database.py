import sqlite3
import datetime

connection = sqlite3.connect("data.db")

# SQL COMMANDS

CREATE_MOVIES_TABLE = """
create table if not exists movies (
    title TEXT,
    release_timestamp REAL,
    watched INTEGER);"""

INSERT_MOVIES = """
insert into movies (title, release_timestamp, watched) values (?,?,0);"""

SELECT_ALL_MOVIES = """
select title, release_timestamp, watched from movies;"""

SELECT_UPCOMING_MOVIES = """
select title, release_timestamp, watched from movies where release_timestamp > ?;"""

SELECT_WATCHED_MOVIES = """
select title, release_timestamp, watched from moves where watched = 1;"""

# SQL METHODS

def create_tables():
    with connection:
        connection.execute(CREATE_MOVIES_TABLE)

def add_movie(title, release_timestamp):
    with connection:
        connection.execute(INSERT_MOVIES, (title, release_timestamp))

def get_movies(upcoming=False):
    with connection:
        cursor = connection.cursor()
        if upcoming:
            today_timestamp = datetime.datetime.today().timestamp()
            cursor.execute(SELECT_UPCOMING_MOVIES, (today_timestamp,))
        else:
            cursor.execute(SELECT_ALL_MOVIES)
        return cursor.fetchall()

def watch_movie(title):
    with connection:
        today_timestamp = datetime.datetime.today().timestamp()
        connection.execute(INSERT_MOVIES, (title, today_timestamp))

def get_watched_movies():
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_WATCHED_MOVIES)
        return cursor.fetchall()
