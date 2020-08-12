import database
import datetime

menu = """Please select one of the following options:
1) Add new movie.
2) View upcoming movies.
3) View all movies
4) Watch a movie
5) View watched movies.
6) Exit.

Your selection: """
welcome = "Welcome to the watchlist app!"

print(welcome)
database.create_tables()

def add_movie():
    title = input("Movie title: ")
    release_date = input("Release date (dd-mm-yyyy): ")
    parsed_date = datetime.datetime.strptime(release_date, "%d-%m-%Y")
    database.add_movie(title, parsed_date.timestamp())

def print_movies(movies):
    print("-- Movies --")
    for movie in movies:
        movie_timestamp = datetime.datetime.fromtimestamp(movie[1])
        movie_release_date = movie_timestamp.strftime("%b %d %Y")
        print(f"{movie[0]} (released on {movie_release_date})")
    print("--\n")
    print("\n")

def set_watched():
    title = input("Movie title: ")
    database.watch_movie(title)

user_input = input(menu)
while user_input != "6":
    if user_input == "1":
        add_movie()
    elif user_input == "2":
        print_movies(database.get_movies(True))
    elif user_input == "3":
        print_movies(database.get_movies(False))
    elif user_input == "4":
        set_watched()
    elif user_input == "5":
        print_movies(database.get_watched_movies())
    else:
        print("Invalid input, please try again!")
    user_input = input(menu)
