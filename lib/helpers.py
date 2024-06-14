# lib/helpers.py
from models.books import Book
from models.magazines import Magazine
from models.movies import Movie
from models.music import Music




def add_book():
    name = input("Enter name of book here....")
    author = input("Enter name of author here....")
    pages = int(input("Enter number of pages here...."))
    price = float(input("Enter book price here...."))
    try:
        books = Book.create(name, author, pages, price)
        print (f"Book: {books} added successfully to catalogue")
    except Exception as e:
       print(f"Error: {e}")

def del_book():
    _name_ = input("Enter name for book to delete here....")
    book = Book.find_by_name(_name_)
    if book:
        book.delete()
        print(f"{_name_} deleted successfully from catalogue")
    else:
        print(f"{_name_} not found in catalogue")


def list_books():
    books = Book.get_all()
    if not books:
        print("No books available in the catalogue.")
    else:
        print("Available books in catalogue:")
        for book in books:
            print(book)


def search_bookname():
    name_prefix = input("Enter the starting letters of the book name: ")
    books = [book for book in Book.get_all() if book.name.startswith(name_prefix)]
    if books:
        print("Books matching the search:")
        for book in books:
            print(book)
    else:
        print("No books found matching the search criteria.")


def purchase_book():
    name =input("Enter name of book to purchase here....")
    book = Book.find_by_name(name)
    print (f"Purchasd {book.name} successfully for {book.price}")



def add_magazine():
    name = input("Enter name of magazine here....")
    publisher = input("Enter name of publisher here....")
    year = int(input("Enter year of publishing here...."))
    price = float(input("Enter magazine price price here...."))
    try:
       magazines = Magazine.create(name, publisher, year, price)
       print(f"Success :{magazines} added successfully to catalogue")
    except Exception as e:
       print(f"Error: {e}")

def del_magazine():
    _name_ = input("Enter name....")
    magazine = Magazine.find_by_name(_name_)
    if magazine:
        magazine.delete()
        print(f"{_name_} deleted successfully from catalogue")
    else:
        print(f"{_name_} not found in catalogue")



def list_magazine():
    magazines = Magazine.get_all()
    if not magazines:
        print("No magazines available in the catalogue.")
    else:
        print("Available magazines in catalogue:")
        for magazine in magazines:
            print(magazine)


def search_magazinename():
    name_prefix = input("Enter the starting letters of the magazine name: ")
    magazines = [magazine for magazine in Magazine.get_all() if magazine.name.startswith(name_prefix)]
    if magazines:
        print("Magazines matching the search:")
        for magazine in magazines:
            print(magazine)
    else:
        print("No magazines found matching the search criteria.")


def purchase_magazine():
    name =input("Search name of magazine to purchase here.....")
    magazine = Magazine.find_by_name(name)
    print (f"Purchased {magazine.name} successfully for {magazine.price}")



def add_movie():
    name = input("Enter name of movie here....")
    genre = input("Enter name of genre here....")
    year = int(input("Enter year of release here...."))
    price = float(input("Enter movie price here...."))
    try:
        movie = Movie.create(name, genre, year, price)
        print (f"Movie: {movie} added successfully to catalogue")
    except Exception as e:
       print(f"Error: {e}")

def del_movie():
    _name_ = int(input)
    movie = Movie.find_by_name(_name_)
    if movie:
        movie.delete()
        print(f"{_name_} deleted successfully from catalogue")
    else:
        print(f"{_name_} not found in catalogue")


def list_movies():
    movies = Movie.get_all()
    if not movies:
        print("No movies available in the catalogue.")
    else:
        print("Available movies in catalogue:")
        for movie in movies:
            print(movie)

def search_moviename():
    name_prefix = input("Enter the starting letters of the movie name: ")
    movies = [movie for movie in Movie.get_all() if movie.name.startswith(name_prefix)]
    if movies:
        print("Movies matching the search:")
        for movie in movies:
            print(movie)
    else:
        print("No movies found matching the search criteria.")


def purchase_movie():
    name =input("Search name of movie to purchase here.....")
    movie = Movie.find_by_name(name)
    print (f"Purchased {movie.name} successfully for {movie.price}")



def add_music():
    name = input("Enter name of music here....")
    artist = input("Enter name of artist here....")
    genre = input("Enter music genre here....")
    year = int(input("Enter year of release here...."))
    price = float(input("Enter music price here...."))
    try:
        music = Music.create(name, artist, genre, year, price)
        print (f"Music: {music} added successfully to catalogue")
    except Exception as e:
       print(f"Error: {e}")

def del_music():
    _name_ = int(input)
    music = Book.find_by_name(_name_)
    if music:
        music.delete()
        print(f"{_name_} deleted successfully from catalogue")
    else:
        print(f"{_name_} not found in catalogue")


def list_music():
    musics = Music.get_all()
    if not musics:
        print("No music available in the catalogue.")
    else:
        print("Available music in catalogue:")
        for music in musics:
            print(music)

def search_musicname():
    name_prefix = input("Enter the starting letters of the music name: ")
    music = Music.find_by_name_prefix(name_prefix)
    if music:
        print("Music matching the search:")
        print(music)
    else:
        print("No music found matching the search criteria.")


def purchase_music():
    name =input("Search name of music to purchase here.....")
    music = Music.find_by_name(name)
    print (f"Purchased {music.name} successfully for {music.price}")