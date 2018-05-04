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
                            name TEXT NOT NULL,
                            location_id INTEGER NOT NULL
                            )''')
        self.curr.execute('''CREATE TABLE IF NOT EXISTS observations (
                            id INTEGER PRIMARY KEY,
                            date TEXT NOT NULL,
                            temperature FLOAT NOT NULL,
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

    def add_animal(self, animal_name, location_name):
        """Add an animal from a given location to the database.

        Args:
            animal_name (str): The name of the animal.
            location_name (str): The location where the animal was seen.
        """
        self.curr.execute('''INSERT INTO animals (name, location_id) VALUES (
                            ?, (SELECT locations.id FROM locations
                            WHERE locations.name = ?))''', (animal_name,
                                                            location_name))
        self.conn.commit()

    def get_locations(self):
        """Return a list of all of the location names."""
        names = [x[0] for x in self.curr.execute("SELECT name FROM locations")]
        return names

    def get_animals_from(self, location):
        """Return a list of the animals associated with a given location.

        Args:
            location (str): The location name for the desired list of animals.
        """
        names = [x[0] for x in self.curr.execute('''SELECT name FROM animals
                WHERE location_id = (SELECT locations.id FROM locations WHERE
                locations.name = ?)''', (location,))]
        return names

    def add_observation(self, date, location, animal, amount, temperature):
        """Add a single observation to the database.

        Args:
            date (str): The date of the observation.
            location (str): The location where the observation took place.
            animal (str): The animal name associated with the observation.
            amount (int): The quantity of the animal that was seen.
            temperature (float): The temperature of the water at the time.
        """
        self.curr.execute("""
            INSERT INTO observations (
            date, temperature, location_id, animal_id, amount)
            VALUES (?, ?, (SELECT id FROM locations WHERE name = ?),
            (SELECT id FROM animals WHERE name = ?
            AND location_id = (SELECT id FROM locations WHERE name = ?)), ?)
            """, (date, temperature, location, animal, location, amount))

        self.conn.commit()

    def get_observations(self, animal, location):
        """Return observations for a given animal and location.

        Args:
            animal (str): The animal name.
            location (str): The location name.
        Returns:
            A tuple of 3 lists:
            The first list contains date strings.
            The second list contains corresponding population sizes.
            The third list contains corresponding temperatures.
        """
        self.curr.execute("""
            SELECT date, amount, temperature
            FROM observations, locations, animals
            WHERE observations.location_id = locations.id
            AND observations.animal_id = animals.id
            AND locations.name = ?
            AND animals.name = ?
            ORDER BY date ASC
            """, (location, animal))
        
        rows = self.curr.fetchall()
        return ([x[0] for x in rows],
                [x[1] for x in rows],
                [x[2] for x in rows])

    def delete_animal(self, animal, location):
        """Delete an animal given a location.

        Args:
            animal (str): The animal name to delete.
            location (str): The location of the animal.
        """
        self.curr.execute("""
            DELETE FROM observations
            WHERE observations.animal_id
                = (SELECT id FROM animals WHERE name = ?)
            AND observations.location_id
                = (SELECT id FROM locations WHERE name = ?)
            """, (animal, location))
        self.curr.execute("""
            DELETE FROM animals
            WHERE name = ?
            AND location_id = (SELECT id FROM locations WHERE name = ?)
            """, (animal, location))
        self.conn.commit()

    def delete_location(self, location):
        """Delete a given location.

        Args:
            location (str): The name of the location to delete.
        """
        self.curr.execute("""
            SELECT id FROM locations WHERE name = ?
            """, (location,))

        location_id = (self.curr.fetchone())[0]

        self.curr.execute("""
            DELETE FROM observations
            WHERE observations.location.id = ?
            """, (location_id,))

        self.curr.execute("""
            DELETE FROM animals
            WHERE animals.location.id = ?
            """, (location_id,))

        self.curr.execute("""
            DELETE FROM locations
            WHERE locations.id = ?
            """, (location_id,))

        self.conn.commit()

    def commit(self):
        self.conn.commit()

    def close(self):
        self.curr.close()
        self.conn.close()
