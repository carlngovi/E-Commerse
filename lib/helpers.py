# lib/helpers.py
from models.books import Book
from models.magazines import Magazine
from models.movies import Movie
from models.music import Music


def book_cat():
    all = [] 

def add_book():
    name = input("Enter name of book here....")
    author = input("Enter name of author here....")
    pages = int(input("Enter number of pages here...."))
    price = float(input("Enter book price here...."))
    try:
        books = Book.create(name, author, pages, price)
        print (f"Book: {books} added successfully")
    except Exception as e:
       print(f"Error: {e}")

def del_book():
    _name_ = input("Enter name for book to delete here....")
    if book := Book.find_by_name(_name_):
        book.delete()
        print (f"{_name_} deleted successfully")
    else:
        print(f"{_name_} not found in catalogue")

def list_books():
    books = Book.get_all()
    for book in books:
        print(f"Available books in catalogue \n {book}")


def search_bookname():
    name =input("Search book by name here....")
    book = Book.find_by_name(name)
    print (f"{book}")

def purchase_book():
    name =input("Enter name of book to purchase here....")
    book = Book.find_by_name(name)
    print (f"Purchasd {book.name} successfully for {book.price}")

def magazine_cat():
    all = [] 

def add_magazine():
    name = input("Enter name of magazine here....")
    publisher = input("Enter name of publisher here....")
    year = int(input("Enter year of publishing here...."))
    price = float(input("Enter magazine price price here...."))
    try:
       magazines = Magazine.create(name, publisher, year, price)
       print(f"Success :{magazines} added successfully")
    except Exception as e:
       print(f"Error: {e}")

def del_magazine():
    _name_ = input("Enter name....")
    if magazine := Magazine.find_by_name(_name_):
        magazine.delete()
        print (f"Magazine: {_name_} deleted successfully")
    else:
        print(f"Magazine: {_name_} not found in catalogue")


def list_magazine():
    magazines = Magazine.get_all()
    for magazine in magazines:
        print(f"Available magazines in catalogue \n {magazine}")


def search_magazinename():
    name =input("Search magazine by name here.....")
    magazine = Magazine.find_by_name(name)
    print (f"{magazine}")

def purchase_magazine():
    name =input("Search name of magazine to purchase here.....")
    magazine = Magazine.find_by_name(name)
    print (f"Purchased {magazine.name} successfully for {magazine.price}")

def movie_cat():
    all = [] 

def add_movie():
    name = input("Enter name of movie here....")
    genre = input("Enter name of genre here....")
    year = int(input("Enter year of release here...."))
    price = float(input("Enter movie price here...."))
    try:
        movie = Movie.create(name, genre, year, price)
        print (f"Movie: {movie} added successfully")
    except Exception as e:
       print(f"Error: {e}")

def del_movie():
    _name_ = int(input)
    if movie := Movie.find_by_name(_name_):
        movie.delete()
        print (f"Movie: {_name_} deleted succesfully")
    else:
        print(f"Movie: {_name_}not found in catalogue")

def list_movies():
    movies = Movie.get_all()
    for movie in movies:
        print(f"Available movies in catalogue \n {movie}")

def search_moviename():
    name =input("Search movie by name here.....")
    movie = Movie.find_by_name(name)
    print (f"{movie}")

def purchase_movie():
    name =input("Search name of movie to purchase here.....")
    movie = Movie.find_by_name(name)
    print (f"Purchased {movie.name} successfully for {movie.price}")

def music_cat():
    all = []

def add_music():
    name = input("Enter name of music here....")
    artist = input("Enter name of artist here....")
    genre = input("Enter music genre here....")
    year = int(input("Enter year of release here...."))
    price = float(input("Enter music price here...."))
    try:
        music = Music.create(name, artist, genre, year, price)
        print (f"Music: {music} added successfully")
    except Exception as e:
       print(f"Error: {e}")

def del_music():
    _name_ = int(input)
    if music := Music.find_by_name(_name_):
        music.delete()
        print (f"Music: {_name_} deleted successfully")
    else:
        print(f"Music {_name_} not found in catalogue")

def list_music():
    musics = Music.get_all()
    for music in musics:
        print(f"Available music in catalogue \n {music}")

def search_musicname():
    name =input("Search music by name here.....")
    music = Music.find_by_name(name)
    print (f"{music}")

def purchase_music():
    name =input("Search name of music to purchase here.....")
    music = Music.find_by_name(name)
    print (f"Purchased {music.name} successfully for {music.price}")