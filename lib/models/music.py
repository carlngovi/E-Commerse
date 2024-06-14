from models.__init__ import CONN, CURSOR


class Music():
    all = {}

    def __init__(music, name, artist, genre, year, price):
        music.name = name
        music.artist = artist
        music.genre = genre
        music.year = year
        music.price = price

    def __repr__(music):
        return f"ID: {music.id}, Name: {music.name}, Artist: {music.artist}, Genre: {music.genre}, Year: {music.year}, Price: ${music.price}"

    @property
    def name(music):
        return music._name

    @name.setter
    def name(music, name):
        if isinstance(name, str):
            music._name = name
        else:
            raise ValueError(" must be a non-empty string")
        
    @property
    def artist(music):
        return music._artist
    
    @artist.setter
    def artist(music, artist):
        if isinstance(artist, str):
            music._artist = artist
        else:
            raise ValueError("must be a non empty string")

    @property
    def genre(music):
        return music._publisher

    @genre.setter
    def genre(music, genre):
        if isinstance(genre, str):
            music._publisher = genre
        else:
            raise ValueError(" must be a non-empty string")

    @property
    def year(music):
        return music._year

    @year.setter
    def year(music, year):
        if isinstance(year, int):
            music._year = year
        else:
            raise ValueError(" must be a number")

    @property
    def price(music):
        return music._price

    @price.setter
    def price(music, price):
        if isinstance(price, float): 
            music._price = price
        else:
            raise ValueError(" must be a number")

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS music (
            Id INTEGER PRIMARY KEY,
            Name TEXT,
            Artist TEXT,
            Genre TEXT,
            Year  INTEGER,
            Price INTEGER)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS music ;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(music):
        sql = """
            INSERT INTO music (Name, Artist, Genre, Year, Price)
            VALUES (?, ?, ?, ?, ?)
        """
        try:
            CURSOR.execute(sql, (music.name, music.author, music.pages, music.price))
            CONN.commit()
            music.id = CURSOR.lastrowid
            type(music).all[music.id] = music
        except Exception as e:
            CONN.rollback()
            print(f"Error saving music: {e}")

    @classmethod
    def create(cls, name, artist, genre, year, price):
        music = cls(name,artist, genre, year, price)
        music.save()
        return music

    def delete(music):
        sql = """
            DELETE FROM music
            WHERE id = ?
        """
        CURSOR.execute(sql, (music.id,))
        CONN.commit()
        del type(music).all[music.id]
        music.id = None

    @classmethod
    def instance_from_db(cls, row):
        music = cls.all.get(row[0])
        if music:
            music.name = row[1]
            music.artist = row[2]
            music.genre = row[3]
            music.year = int(row[4])
            music.price = float(row[5])
        else:
            music = cls(row[1], row[2], row[3], int(row[3]), float(row[4]))
            music.id = row[0]
            cls.all[music.id] = music
        return music

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM music
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM music
            WHERE name = ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_author(cls, genre):
        sql = """
            SELECT *
            FROM music
            WHERE genre = ?
        """
        row = CURSOR.execute(sql, (genre,)).fetchone()
        return cls.instance_from_db(row) if row else None
        
Music.create_table()