import database
import datetime

menu = """Please select one of the following options:
0) Add a user.
1) Add new movie.
2) View upcoming movies.
3) View all movies
4) Watch a movie
5) View watched movies.
6) List users.
7) Exit.

Your selection: """
welcome = "Welcome to the watchlist app!"

print(welcome)
database.create_tables()

def add_user():
    name = input("User name: ")
    database.add_user(name)

def get_users():
    users = database.get_users()
    print("-- Users --")
    for user in users:
        print(f"{user[0]} {user[1]}")
    print("--\n\n")

def add_movie():
    title = input("Movie title: ")
    release_date = input("Release date (dd-mm-yyyy): ")
    parsed_date = datetime.datetime.strptime(release_date, "%d-%m-%Y")
    database.add_movie(title, parsed_date.timestamp())

def print_movies(movies):
    print("-- Movies --")
    for movie in movies:
        movie_timestamp = datetime.datetime.fromtimestamp(movie[2])
        movie_release_date = movie_timestamp.strftime("%b %d %Y")
        print(f"{movie[0]} {movie[1]} (released on {movie_release_date})")
    print("--\n\n")

def print_watched_movies(movies):
    print("-- Movies --")
    for movie in movies:
        print(f"{movie[0]}")
    print("--\n")
    print("\n")

def set_watched():
    title = input("Movie Id: ")
    watcher = input("User Id: ")
    database.watch_movie(title, watcher)

def get_watched():
    watcher_name = input("Watcher name: ")
    print_watched_movies(database.get_watched_movies(watcher_name))

def get_movies(upcoming):
    print_movies(database.get_movies(upcoming))

user_input = input(menu)
while user_input != "7":
    if user_input == "0":
        add_user()
    elif user_input == "1":
        add_movie()
    elif user_input == "2":
        get_movies(True)
    elif user_input == "3":
        get_movies(False)
    elif user_input == "4":
        set_watched()
    elif user_input == "5":
        get_watched()
    elif user_input == "6":
        get_users()
    else:
        print("Invalid input, please try again!")
    user_input = input(menu)
