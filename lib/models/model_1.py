from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker


# Define the database URL (SQLite in this case)
DATABASE_URL = 'sqlite:///ecommerse.db'

# Create an engine
engine = create_engine(DATABASE_URL)

# Define a base class for the declarative model
Base = declarative_base()

# Define the Book class
class Book(Base):
    __tablename__ = 'Books'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    author = Column(String, nullable=False)
    pages = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)

class Magazine(Base):
    __tablename__ = 'Magazines'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    publisher = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)

class Movie(Base):
    __tablename__ = 'Movies'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    genre = Column(String, nullable=False)
    release = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)

class Music(Base):
    __tablename__ = 'Music'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    artist = Column(String, nullable=False)
    genre = Column(String, nullable=False)
    release = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)

# Create the table in the database
Base.metadata.create_all(engine)

# Create a session maker
Session = sessionmaker(bind=engine)

def model_1():
    session = Session()

    choice = 0
    while choice != 5:
        print("***Welcome to the ecommerce***")
        print("1) Books")
        print("2) Magazines")
        print("3) Movies")
        print("4) Music")
        print("5) Quit")
        choice = int(input())

        if choice == 1:
            while choice !=5:
                print("*** Books Category ***")
                print("1) Add a book for sale")
                print("2) Display available books")
                print("3) Purchase a book")
                print("4) Remove book from catalogue")
                print("5) Return")
                choice = int(input())

                if choice == 1:
                    nBook = input("Enter the name of the book >>> ")
                    nAuthor = input("Enter the name of the author >>> ")
                    nPages = int(input("Enter the number of pages >>> "))
                    nPrice = float(input("Enter the price of the book >>>"))
                    print("Adding a book...")
                    new_book = Book(name=nBook, author=nAuthor, pages=nPages, price =nPrice)
                    session.add(new_book)
                    session.commit()
                    print("Book added successfully.")
        
                elif choice == 2:
                    print("Displaying all books...")
                    books = session.query(Book).all()
                    if books:
                        for book in books:
                            print(f"ID: {book.id}, Name: {book.name}, Author: {book.author}, Pages: {book.pages}, Price: ${book.price}")
                    else:
                        print("No books available.")
                    
        
                elif choice == 3:
                    keyword = input("Search book by name: ")
                    print("Looking up for a book...")
                    books = session.query(Book).filter(Book.name.contains(keyword)).all()
                    if books:
                        for book in books:
                            print(f"ID: {book.id}, Name: {book.name}, Author: {book.author}, Pages: {book.pages}, Price: ${book.price}")
                            print(f"1) Purchase {book.name}")
                            print("2) Return")
                            choice = int(input())

                            if choice == 1:
                                print(f"Purchased {book.name} succesful for ${book.price}")
                            elif choice == 2:
                                print("Returning")
                    else :
                        print ("No book found")

                elif choice == 4:
                    book_id = int(input("Enter the ID of the book to delete: (E.G: 1, 2)"))
                    print(f"Deleting a book with book id:{book_id}...")
                    book = session.query(Book).filter(Book.id == book_id).first()
                    if book:
                        session.delete(book)
                        session.commit()
                        print("Book deleted successfully.")
                    else:
                        print("Book not found.")

                elif choice == 5:
                    print("***returning***")

        if choice == 2:
            while choice != 5:
                print("*** Magazine Catalogue ***")
                print("1) Add a magazine for sale ")
                print("2) Display availabe magazine")
                print("3) Purchase a magazine")
                print("4) Remove magazine from catalogue")
                print("5) Return")
                choice = int(input())

                if choice == 1:
                    nMagazine = input("Enter the name of the magazine >>> ")
                    nPublisher = input("Enter the publisher of the magazine >>> ")
                    nYear = int(input("Enter the year of publishing >>> "))
                    nPrice = float(input("Enter price of the magazine >>>"))
                    print("Adding a magazine...")
                    new_magazine = Magazine(name=nMagazine, publisher=nPublisher, year=nYear, price=nPrice)
                    session.add(new_magazine)
                    session.commit()
                    print("Magazine added successfully.")
    
                elif choice == 2:
                    print("Displaying all magazines...")
                    magazines = session.query(Magazine).all()
                    if magazines:
                        for magazine in magazines:
                            print(f"ID: {magazine.id}, Name: {magazine.name}, Publisher: {magazine.publisher},Year of Publish: {magazine.year}, Price: ${magazine.price}")
                    else:
                        print("No magazines available.")
                    
        
                elif choice == 3:
                    keyword = input("Search magazine by name: ")
                    print("Looking up for a magazines...")
                    magazines = session.query(Magazine).filter(Magazine.name.contains(keyword)).all()
                    if magazines:
                        for magazine in magazines:
                            print(f"ID: {magazine.id}, Name: {magazine.name}, Publisher: {magazine.publisher},Year of Publish:{magazine.year}, Price: ${magazine.price}")
                            print(f"1) Purchase {magazine.name}")
                            print("2) Return")
                            choice = int(input())

                            if choice == 1:
                                print(f"Purchased {magazine.name} succesful for ${magazine.price}")
                            elif choice == 2:
                                print("Returning")
                    else :
                        print ("No magazine found")

                elif choice == 4:
                    magazine_id = int(input("Enter the ID of the magazine to delete: (E.G: 1, 2)"))
                    print(f"Deleting the magazine wih magazine id:{magazine_id}...")
                    magazine = session.query(Magazine).filter(Magazine.id == magazine_id).first()
                    if magazine:
                        session.delete(magazine)
                        session.commit()
                        print("Magazine deleted successfully.")
                    else:
                        print("Magazine not found.")

                elif choice == 5:
                    print("***returning back***")

        if choice == 3:
            while choice !=5:
                print("*** Movie Catalogue ***")
                print("1) Add a movie")
                print("2) Display available movies")
                print("3) Purchase a movie")
                print("4) Remove movie from catalogue")
                print("5) Rerturn")
                choice = int(input())
        
                if choice == 1:
                    nMovie = input("Enter the name of the movie >>> ")
                    nGenre = input("Enter the movie genre >>>")
                    nRelease = int(input("Enter the year of movie release >>>"))
                    nPrice = float(input("Enter the price of the movie >>>"))
                    print("Adding a movie...")
                    new_movie = Movie(name=nMovie,genre=nGenre, release=nRelease, price=nPrice)
                    session.add(new_movie)
                    session.commit()
                    print("Movie added successfully.")
        
                elif choice == 2:
                    print("Displaying all moviess...")
                    movies = session.query(Movie).all()
                    if movies:
                        for movie in movies:
                            print(f"ID: {movie.id}, Name: {movie.name},Genre: {movie.genre}, Release: {movie.release}, Price: ${movie.price}")
                            
                    else:
                        print("No movies available.")
        
                elif choice == 3:
                    keyword = input("Search movie by name: ")
                    print("Looking for a movie...")
                    movies = session.query(Movie).filter(Movie.name.contains(keyword)).all()
                    if movies:
                        for movie in movies:
                            print(f"ID: {movie.id}, Name: {movie.name}, Genre: {movie.genre}, Release: {movie.release}, Price: ${movie.price}")
                            print(f"1) Purchase {movie.name}")
                            print("2) Return")
                            choice = int(input())

                            if choice == 1:
                                print(f"Purchased {movie.name}succesful for ${movie.price}")
                            elif choice == 2:
                                    print("Returning")
                    else:
                        print("No movies found.")

                elif choice == 4:
                    movie_id = int(input("Enter the ID of the movie to delete: (E.G: 1, 2)"))
                    print(f"Deleting the movie with movie id:{movie_id}...")
                    movie = session.query(Movie).filter(Movie.id == movie_id).first()
                    if movie:
                        session.delete(movie)
                        session.commit()
                        print("Movie deleted successfully.")
                    else:
                        print("Movie not found.")

                elif choice == 5:
                    print("***returning back***")

        if choice == 4:
            while choice !=5:
                print("*** Music Catalogue ***")
                print("1) Add music")
                print("2) Display available music")
                print("3) Purchase music")
                print("4) Remove music from catalogue")
                print("5) Return")
                choice = int(input())
        
                if choice == 1:
                    nMusic = input("Enter the name of the music >>> ")
                    nArtist = input("Enter the name of the artist >>>")
                    nGenre = input("Enter the music genre >>>")
                    nRelease = int(input("Enter the year of music release >>>"))
                    nPrice = float(input("Enter the price of the music >>>"))
                    print("Adding music...")
                    new_music = Music(name=nMusic, artist=nArtist, genre=nGenre, release=nRelease, price=nPrice)
                    session.add(new_music)
                    session.commit()
                    print("Music added successfully.")
        
                elif choice == 2:
                    print("Displaying all available music...")
                    musics = session.query(Music).all()
                    if musics:
                        for music in musics:
                            print(f"ID: {music.id}, Name: {music.name}, Artist: {music.artist}, Genre: {music.genre}, Release: {music.release}, Price: ${music.price}")
                            
                    else:
                        print("No such music available.")
        
                elif choice == 3:
                    keyword = input("Search music by name: ")
                    print("Looking for music...")
                    musics = session.query(Music).filter(Music.name.contains(keyword)).all()
                    if musics:
                        for musics in musics:
                            print(f"ID: {music.id}, Name: {music.name}, Artist: {music.artist}, Genre: {music.genre}, Release: {music.release}, Price: ${music.price}")
                            print(f"1) Purchase {music.name}")
                            print("2) Return")
                            choice = int(input())

                            if choice == 1:
                                print(f"Purchased {music.name} by {music.artist} succesful for ${music.price}")
                            elif choice == 2:
                                    print("Returning")
                    else:
                        print("No such music found.")

                elif choice == 4:
                    music_id = int(input("Enter the ID of the music to delete: (E.G: 1, 2)"))
                    print(f"Deleting the music with music id:{music_id}...")
                    music = session.query(Music).filter(Music.id == music_id).first()
                    if music:
                        session.delete(music)
                        session.commit()
                        print("Music deleted successfully.")
                    else:
                        print("Music not found.")
        
                elif choice == 5:
                    print("***returning back***")
    session.close()
    print("Program ended!")

if __name__ == "__main__":
    model_1()