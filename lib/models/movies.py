from models.__init__ import CONN, CURSOR


class Movie():
    all = {}

    def __init__(movie, name, genre, year, price):
        movie.name = name
        movie.genre = genre
        movie.year = year
        movie.price = price

    def __repr__(movie):
        return f"ID: {movie.id}, Name: {movie.name}, Genre: {movie.genre}, Year: {movie.year}, Price: ${movie.price}"

    @property
    def name(movie):
        return movie._name

    @name.setter
    def name(movie, name):
        if isinstance(name, str):
            movie._name = name
        else:
            raise ValueError(" must be a non-empty string")

    @property
    def genre(movie):
        return movie._genre

    @genre.setter
    def genre(movie, genre):
        if isinstance(genre, str):
            movie._genre = genre
        else:
            raise ValueError(" must be a non-empty string")

    @property
    def year(movie):
        return movie._year

    @year.setter
    def year(movie, year):
        if isinstance(year, int):
            movie._year = year
        else:
            raise ValueError(" must be a number")

    @property
    def price(movie):
        return movie._price

    @price.setter
    def price(movie, price):
        if isinstance(price, float): 
            movie._price = price
        else:
            raise ValueError(" must be a number")

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS movies (
            Id INTEGER PRIMARY KEY,
            Name TEXT,
            Genre TEXT,
            Year INTEGER,
            Price INTEGER)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS movies;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(movie):
        sql = """
            INSERT INTO movies (Name, Genre, Year, Price)
            VALUES (?, ?, ?, ?)
        """
        try:
            CURSOR.execute(sql, (movie.name, movie.author, movie.pages, movie.price))
            CONN.commit()
            movie.id = CURSOR.lastrowid
            type(movie).all[movie.id] = movie
        except Exception as e:
            CONN.rollback()
            print(f"Error saving movie: {e}")

    @classmethod
    def create(cls, name, genre, year, price):
        movie = cls(name, genre, year, price)
        movie.save()
        return movie

    def delete(movie):
        sql = """
            DELETE FROM movies
            WHERE id = ?
        """
        CURSOR.execute(sql, (movie.id,))
        CONN.commit()
        del type(movie).all[movie.id]
        movie.id = None

    @classmethod
    def instance_from_db(cls, row):
        movie = cls.all.get(row[0])
        if movie:
            movie.name = row[1]
            movie.genre = row[2]
            movie.year = int(row[3])
            movie.price = float(row[4])
        else:
            movie = cls(row[1], row[2], int(row[3]), float(row[4]))
            movie.id = row[0]
            cls.all[movie.id] = movie
        return movie

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM movies
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM movies
            WHERE name = ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
        
Movie.create_table()