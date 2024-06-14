from models.__init__ import CONN, CURSOR

class Book():
    all = {}

    def __init__(book, name, author, pages, price ):
        book.name = name
        book.author = author
        book.pages = pages
        book.price = price

    def __repr__(book):
        return f"ID: {book.id}, Name: {book.name}, Author: {book.author}, Pages: {book.pages}, Price: ${book.price}"

    @property
    def name(book):
        return book._name

    @name.setter
    def name(book, name):
        if isinstance(name, str):
            book._name = name
        else:
            raise ValueError(" must be a non-empty string")

    @property
    def author(book):
        return book._author

    @author.setter
    def author(book, author):
        if isinstance(author, str):
            book._author = author
        else:
            raise ValueError(" must be a non-empty string")

    @property
    def pages(book):
        return book._pages

    @pages.setter
    def pages(book, pages):
        if isinstance(pages, int):
            book._pages = pages
        else:
            raise ValueError(" must be a number")

    @property
    def price(book):
        return book._price

    @price.setter
    def price(book, price):
        if isinstance(price, float):
            book._price = price
        else:
            raise ValueError(" must be a number")

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS books (
            Id INTEGER PRIMARY KEY,
            Name TEXT,
            Author TEXT,
            Pages INTEGER,
            Price FLOAT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS ;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(book):
        sql = """
            INSERT INTO books (Name, Author, Pages, Price)
            VALUES (?, ?, ?, ?)
        """
        try:
            CURSOR.execute(sql, (book.name, book.author, book.pages, book.price))
            CONN.commit()
            book.id = CURSOR.lastrowid
            type(book).all[book.id] = book
        except Exception as e:
            CONN.rollback()
            print(f"Error saving book: {e}")

    @classmethod
    def create(cls, name, author, pages, price):
        book = cls(name, author, pages, price)
        book.save()
        return book

    def delete(book):
        sql = """
            DELETE FROM books
            WHERE name = ?
        """
        CURSOR.execute(sql, (book.name,))
        CONN.commit()
        del type(book).all[book.id]
    

    @classmethod
    def instance_from_db(cls, row):
        book = cls.all.get(row[0])
        if book:
            book.name = row[1]
            book.author = row[2]
            book.pages = int(row[3])
            book.price = float(row[4])
        else:
            book = cls(row[1], row[2], int(row[3]), float(row[4]))
            book.id = row[0]
            cls.all[book.id] = book
        return book

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM books
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM books
            WHERE name = ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

        
Book.create_table()