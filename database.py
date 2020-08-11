def create_tables():
    pass

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
select title, release_timestamp, watched from movies where release_timestamp >= ?;"""

SELECT_WATCHED_MOVIES = """
select title, release_timestamp, watched from moves where watched = 1;"""

