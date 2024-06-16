# lib/cli.py

from helpers import (

    add_book,
    del_book,
    list_books,
    search_bookname,
    purchase_book,

    add_magazine,
    del_magazine,
    list_magazine,
    search_magazinename,
    purchase_magazine,

    add_movie,
    del_movie,
    list_movies,
    search_moviename,
    purchase_movie,

    add_music,
    del_music,
    list_music,
    search_musicname,
    purchase_music
)


def main():
    print("Welcome, to E-Comm \nAn E-commerse platform")
    print("Enter any number to proceed and 98 to exit")
    choice =int(input("input choice...."))
    while choice != 98:

        menu()

        choice =int(input("input choice...."))
        if choice == 1:
            print("***WELCOME TO THE BOOK CATALOGUE***")
            while choice != 5:
                book_menu()
                choice =int(input("input choice...."))
                if choice == 1:
                    print("********")
                    book_management()
                    while choice != 3:
                        choice =int(input("input choice...."))
                        if choice == 1:
                            add_book()
                        elif choice == 2:
                            del_book()
                        elif choice == 3:
                            print("***returning***")
                elif choice == 2:
                    list_books()
                elif choice == 3:
                    search_bookname()
                elif choice == 4:
                    purchase_book()
                elif choice == 5:
                    print("***returning***")

        elif choice == 2:
            print("***WELCOME TO THE MAGAZINE CATALOGUE***")
            while choice != 5:
                magazine_menu()
                choice =int(input("input choice...."))
                if choice == 1:
                    print("********")
                    magazine_management()
                    while choice != 3:
                        choice =int(input("input choice...."))
                        if choice == 1:
                            add_magazine()
                        elif choice == 2:
                            del_magazine()
                        elif choice == 3:
                            print("***returning***")
                elif choice == 2:
                    list_magazine()
                elif choice == 3:
                    search_magazinename()
                elif choice == 4:
                    purchase_magazine()
                elif choice == 5:
                    print("***returning***")

        elif choice == 3:
            print("***WELCOME TO THE MOVIE CATALOGUE***")
            while choice != 5:
                movie_menu()
                choice =int(input("input choice...."))
                if choice == 1:
                    print("********")
                    movie_management()
                    while choice != 3:
                        choice =int(input("input choice...."))
                        if choice == 1:
                            add_movie()
                        elif choice == 2:
                            del_movie()
                        elif choice == 3:
                            print("***returning***")
                elif choice == 2:
                    list_movies()
                elif choice == 3:
                    search_moviename()
                elif choice == 4:
                    purchase_movie()
                elif choice == 5:
                    print("***returning***")

        elif choice == 4:
            print("***WELCOME TO THE MUSIC CATALOGUE***")
            while choice != 6:
                music_menu()
                choice =int(input("input choice...."))
                if choice == 1:
                    print("********")
                    add_music()
                    while choice != 3:
                        choice =int(input("input choice...."))
                        if choice == 1:
                            add_music()
                        elif choice == 2:
                            del_music()
                        elif choice == 3:
                            print("***returning***")
                elif choice == 2:
                    list_music()
                elif choice == 3:
                    search_musicname()
                elif choice == 4:
                    purchase_music()
                elif choice == 5:
                    print("***returning***")

        elif choice == 98:
            print("***exiting***")
            print("PROGRAM ENDED SUCCESFULLY")


def menu():
    print("1) Book catalogue")
    print("2) Magazine catalogue")
    print("3) Movie catalogue")
    print("4) Music catalogue")
    print("98) Exit")
        

def book_menu():
    print("1)  Book Management")
    print("2)  List available books")
    print("3)  Search for book in catalogue")
    print("4)  Purchase movie from catalogue")
    print("5)  Return")


def magazine_menu():
    print("1)  Magazine Management")
    print("2)  List available magazines in catalogue")
    print("3)  Search for magazine in catalogue")
    print("4)  Purchase a magazine from catalogue")
    print("5)  Return")

def movie_menu():
    print("1)  Movie Management")
    print("2)  List available movies in catalogue")
    print("3)  Search for movie in catalogue")
    print("4)  Purchase a magazine from catalogue")
    print("5)  Return")

def music_menu ():
    print("1) Add music to catalogue")
    print("2) List available music in catalogue")
    print("3) Search for music in catalogue")
    print("4) Purchase music from catlogue")
    print("5) Return")

def book_management():
    print("1)  Add a book to the catalogue")
    print("2)  Delete a book from the catalogue")
    print("3)  Return")

def magazine_management():
    print("1)  Add a magazine to the catalogue")
    print("2)  Delete a magazine from the catalogue")
    print("3)  Return")

def movie_management():
    print("1)  Add a movie to the catalogue")
    print("2)  Delete a movie from the catalogue")
    print("3)  Return")

def music_management():
    print("1)  Add music to the catalogue")
    print("1)  Delete music from the catalogue")
    print("3)  Return")

if __name__ == "__main__":
    main()
