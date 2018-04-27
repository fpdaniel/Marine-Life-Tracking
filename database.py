import sqlite3


class MarineDatabase:
    """Local database class that holds data."""

    locale = "testing.db"

    def __init__(self):
        """Initialize instance variables and creates connection to the database."""
        self.conn = sqlite3.connect(MarineDatabase.locale)
        self.curr = self.conn.cursor()

    def create_tables(self):
        """Create the tables if they don't exist."""
        self.curr.execute('''CREATE TABLE IF NOT EXISTS locations (
                            id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL
                            )''')
        self.curr.execute('''CREATE TABLE IF NOT EXISTS animals (
                            id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL
                            )''')
        self.curr.execute('''CREATE TABLE IF NOT EXISTS observations (
                            id INTEGER PRIMARY KEY,
                            date TEXT NOT NULL,
                            temperature INTEGER NOT NULL,
                            location_id INTEGER NOT NULL,
                            animal_id INTEGER NOT NULL,
                            amount INTEGER
                            )''')
        self.conn.commit()

    def add_location(self, location_name):
        """Add a location to the database.

        Args:
            location_name (str): The location name.
        """
        self.curr.execute("INSERT INTO locations (name) VALUES (?)",
                          (location_name,))
        self.conn.commit()

    def add_animal(self, animal_name):
        """Add an animal to the database.

        Args:
            animal_name (str): The name of the animal.
        """
        self.curr.execute("INSERT INTO animals (name) VALUES (?)",
                          (animal_name,))
        self.conn.commit()

    def commit(self):
        self.conn.commit()

    def close(self):
        self.curr.close()
        self.conn.close()
