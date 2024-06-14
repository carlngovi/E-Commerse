from models.__init__ import CONN, CURSOR


class Magazine():
    all = {}

    def __init__(magazine, name, publisher, year, price):
        magazine.name = name
        magazine.publisher = publisher
        magazine.year = year
        magazine.price = price

    def __repr__(magazine):
        return f"ID: {magazine.id}, Name: {magazine.name}, Publisher: {magazine.publisher}, Year: {magazine.year}, Price: ${magazine.price}"

    @property
    def name(magazine):
        return magazine._name

    @name.setter
    def name(magazine, name):
        if isinstance(name, str):
            magazine._name = name
        else:
            raise ValueError(" must be a non-empty string")

    @property
    def publisher(magazine):
        return magazine._publisher

    @publisher.setter
    def publisher(magazine, publisher):
        if isinstance(publisher, str):
            magazine._publisher = publisher
        else:
            raise ValueError(" must be a non-empty string")

    @property
    def year(magazine):
        return magazine._year

    @year.setter
    def year(magazine, year):
        if isinstance(year, int):
            magazine._year = year
        else:
            raise ValueError(" must be a number")

    @property
    def price(magazine):
        return magazine._price

    @price.setter
    def price(magazine, price):
        if isinstance(price, float):
            magazine._price = price
        else:
            raise ValueError(" must be a number")

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS magazines (
            Id INTEGER PRIMARY KEY,
            Name TEXT,
            Publisher TEXT,
            Year INTEGER,
            Price INTEGER)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS magazines;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(magazine):
        sql = """
            INSERT INTO magazines (Name, Publisher, Year, Price)
            VALUES (?, ?, ?, ?)
        """
        CURSOR.execute(sql, (magazine.name, magazine.publisher, magazine.year, magazine.price))
        CONN.commit()
        magazine.id = CURSOR.lastrowid
        type(magazine).all[magazine.id] = magazine

    @classmethod
    def create(cls, name, publisher, year, price):
        magazines = cls(name, publisher, year, price)
        magazines.save()
        return magazines

    def delete(magazine):
        sql = """
            DELETE FROM magazines
            WHERE name = ?
        """
        CURSOR.execute(sql, (magazine.name,))
        CONN.commit()
        del type(magazine).all[magazine.name]
        

    @classmethod
    def instance_from_db(cls, row):
        magazine = cls.all.get(row[0])
        if magazine:
            magazine.name = row[1]
            magazine.publisher = row[2]
            magazine.year = int(row[3])
            magazine.price = float(row[4])
        else:
            magazine = cls(row[1], row[2], int(row[3]), float(row[4]))
            magazine.id = row[0]
            cls.all[magazine.id] = magazine
        return magazine

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM magazines
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM magazines
            WHERE name = ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

Magazine.create_table()