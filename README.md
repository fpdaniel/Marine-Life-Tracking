# Marine-Life-Tracking

This application is fairly minimal at the moment and is not a completed project. This application was initially started because we needed to make something for a class.

This application's purpose is to keep track of animals seen in different marine environments and locations. Each location has associated with it a list of animals that is independent of other locations’ lists of animals. The user can also add "observations" for each animal, where they can input the date of the observation, the population size seen on that date, and the temperature of the water on that date. This data is stored for later use so that the user can see a graph of the population size over time for that selected animal. The temperature data is not currently used, but it will be used in future improvements of the program.

The application opens with a list of locations that were previously input by the user, along with an option to add or delete a location, or to select a location that is in the location list. Selecting any of those choices will then cause the program to carry out the respective action.

The application manages its stored information using the SQLite module included in standard Python distributions. The application creates a local database if the database does not exist, and it also creates a connection to that database. The data is then stored or retrieved from that database when a user inputs information or requests information through the GUI.


We were supposed to use open source software and libraries to develop our application, and so we did.

This application was written using Python 3.6.

The libraries/modules used in this program are:
- matplotlib
- sqlite3
- tkinter
