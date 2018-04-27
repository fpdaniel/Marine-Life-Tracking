import sqlite3


class MarineDatabase:
    """Local database class that holds data."""

    locale = "testing.db"

    def __init__(self):
        """Initialize class variables and creates connection to db """
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

    def execute_location(self, location_name):
        self.curr.execute("INSERT INTO locations VALUES (?)", (location_name,))

    def commit(self):
        self.conn.commit()

    def close(self):
        self.curr.close()
        self.conn.close()
