import database
import random
from datetime import timedelta, date

db = database.MarineDatabase()
db.create_tables()

location = 'Huntington Beach'
animal = 'Dolphin'

db.add_location(location)
db.add_animal(animal, location)


def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)


random.seed()

start_date = date(2017, 1, 1)
end_date = date(2017, 7, 1)
for single_date in daterange(start_date, end_date):
    db.add_observation(single_date.strftime("%Y-%m-%d"), location, animal,
                       random.randint(0, 20), random.randint(65, 72))

db.close()
