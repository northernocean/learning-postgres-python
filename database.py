import sqlite3
import datetime

connection = sqlite3.connect("data.db")

# SQL COMMANDS

CREATE_MOVIES_TABLE = """
create table if not exists movies (
    title TEXT,
    release_timestamp REAL);"""

CREATE_WATCHED_TABLE = """
create table if not exists watched (
    title TEXT,
    watcher_name TEXT);"""

INSERT_MOVIE = """
insert into movies (title, release_timestamp) values (?,?);"""

INSERT_WATCHED_MOVIE = """
insert into watched (title, watcher_name) values (?,?);"""

DELETE_MOVIE = """
delete from movies where title = ?;"""

SELECT_ALL_MOVIES = """
select title, release_timestamp from movies;"""

SELECT_UPCOMING_MOVIES = """
select title, release_timestamp from movies where release_timestamp > ?;"""

SELECT_WATCHED_MOVIES = """
select title from watched where watcher_name = ?;"""

# SQL METHODS

def create_tables():
    with connection:
        connection.execute(CREATE_MOVIES_TABLE)
        connection.execute(CREATE_WATCHED_TABLE)

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

def watch_movie(title, watcher_name):
    with connection:
        connection.execute(DELETE_MOVIE, (title,))
        connection.execute(INSERT_WATCHED_MOVIE, (title, watcher_name))

def get_watched_movies(watcher_name):
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_WATCHED_MOVIES, (watcher_name,))
        return cursor.fetchall()
