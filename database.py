import sqlite3

class MarineDatabase:
    """ Local database class that holds data """
    locale = "testing.db"

    def __init__(self):
        """ Initialize class variables and creates connection to db """
        self.conn = sqlite3.connect(MarineDatabase.locale)
        self.curr = self.conn.cursor()

    def create_table_locations(self):
        """ Create table with the name of the table being locations and one column for beach """
        self.curr.execute(''' CREATE TABLE IF NOT EXISTS locations
                              (beach)''')
        self.conn.commit()

    def execute_location(self, location_name):
        self.curr.execute(" INSERT INTO locations VALUES (?)", (location_name,))

    def commit(self):
        self.conn.commit()

    def close(self):
        self.conn.close()