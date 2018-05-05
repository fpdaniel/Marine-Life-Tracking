import tkinter
import tkinter.messagebox

import matplotlib.pyplot as plt

#import sqlite3

species_list = []
location_list = []

date_list = []
population_list = []
temperature_list = []


class MyGUI:
    def __init__(self):
        # Create main window widget
        self.main_window = tkinter.Tk()

        self.main_window.wm_title('Marine Life Tracker')

        # Left Side - List of Locations
        self.firstFrame = tkinter.LabelFrame(self.main_window, text=" Locations ")
        self.firstFrame.grid(row=0, columnspan=10, sticky='NW', rowspan=10, padx=5, pady=5, ipadx=0, ipady=70)

        self.scrollbar1 = tkinter.Scrollbar(self.firstFrame)
        self.scrollbar1.pack(side="right", fill="y")

        self.locationList = tkinter.Listbox(self.firstFrame, yscrollcommand=self.scrollbar1.set)
        self.locationList.pack(side="left", fill="y")
        self.scrollbar1.config(command=self.locationList.yview)

        # Right Side - Buttons
        self.useLocations = tkinter.LabelFrame(self.main_window, text=" Add/Delete/Select ")
        self.useLocations.grid(row=0, column=15, columnspan=15, sticky='NW', rowspan=3, padx=5, pady=5,
                               ipadx=10, ipady=40)

        self.add_location_btn = tkinter.Button(self.useLocations, text="Add Location",
                                               command=self.add_location)
        self.add_location_btn.grid(row=2, column=0, sticky='W', padx=5, pady=2)

        self.delete_location_btn = tkinter.Button(self.useLocations, text="Delete Location",
                                                  command=self.delete_location)
        self.delete_location_btn.grid(row=4, column=0, padx=5, pady=2)

        self.instruction = tkinter.LabelFrame(self.main_window, text="Instructions")
        self.instruction.grid(row=5, column=15, columnspan=15, sticky='NE', rowspan=3, padx=5, pady=5,
                               ipadx=8, ipady=40)

        self.location_instruction = tkinter.Label(self.instruction, text="Double click on location to open new window.")
        self.location_instruction.grid(row=6, column=0, padx=5, pady=2)

        self.locationList.bind('<Double-1>', self.get_location)

        #Enter tkinter loop
        tkinter.mainloop()










#**************************************************************************************
#
#*******************main_functions - First Page ***************************************
#
#**************************************************************************************
    def add_location(self):

        self.root_add_location = tkinter.Tk()
        self.root_add_location.wm_title("Add Location")

        # Create frames
        self.instruction_add_location = tkinter.LabelFrame(self.root_add_location, text="Adding Location")
        self.instruction_add_location.grid(row=0, columnspan=20, sticky='NW',
                                           rowspan=10, padx=5, pady=5, ipadx=10, ipady=4)

        # Create Label for Species Name
        self.label_name = tkinter.Label(self.instruction_add_location, text='Enter Location Name: ')
        self.label_name.grid(row=0, column=0)

        self.location_name_entry = tkinter.Entry(self.instruction_add_location, width=20)
        self.location_name_entry.grid(row=0, column=2, sticky='W')

        # Create button widgets for bottom frame
        self.add_location_button = tkinter.Button(self.instruction_add_location, text='Add Location',
                                                  command=self.adding_location)
        self.add_location_button.grid(row=1, column=0, sticky='E', padx=5, pady=2)

        self.save_button = tkinter.Button(self.instruction_add_location, text='Save & Quit',
                                          command=self.root_add_location.destroy)
        self.save_button.grid(row=1, column=2, sticky='W', padx=5, pady=2)


    def delete_location(self):
        items = self.locationList.curselection()
        pos = 0
        for i in items:
            idx = int(i) - pos
            self.locationList.delete(idx, idx)
            pos = pos + 1

    def get_location(self, event):
        index = self.locationList.curselection()
        label = self.locationList.get(index)
        self.select_location(label)

    def select_location(self, selection):
        location_name = selection

        self.root_select = tkinter.Tk()
        self.root_select.wm_title(location_name)

        # Left Frame - Species List
        self.leftFrame1 = tkinter.LabelFrame(self.root_select, text="Species List")
        self.leftFrame1.grid(row=0, columnspan=10, sticky='NW', rowspan=10, padx=5, pady=5, ipadx=0, ipady=70)

        self.scrollbar2 = tkinter.Scrollbar(self.leftFrame1)
        self.scrollbar2.pack(side="right", fill="y")

        self.speciesList = tkinter.Listbox(self.leftFrame1, yscrollcommand=self.scrollbar2.set)
        self.speciesList.pack(side="left", fill="y")
        self.scrollbar2.config(command=self.speciesList.yview)

        # Right TopFrame - Add Species, Delete Species
        self.speciesFrame = tkinter.LabelFrame(self.root_select, text="Add/Delete Species")
        self.speciesFrame.grid(row=0, column=15, columnspan=15, sticky='NW',
                               rowspan=6, padx=5, pady=5, ipadx=25, ipady=50)

        self.add_species_button = tkinter.Button(self.speciesFrame, text="Add Species",
                                                 command=self.add_species_name)
        self.add_species_button.grid(row=2, column=16, sticky='W', padx=5, pady=2)

        self.delete_species_button = tkinter.Button(self.speciesFrame, text="Delete Species",
                                                    command=self.delete_species_name)
        self.delete_species_button.grid(row=2, column=32, sticky='W', padx=5, pady=2)

        self.instruction_select = tkinter.LabelFrame(self.root_select, text="Instructions")
        self.instruction_select.grid(row=5, column=15, columnspan=15, sticky='NE', rowspan=3, padx=5, pady=5,
                              ipadx=8, ipady=40)

        self.species_instruction = tkinter.Label(self.instruction_select,
                                                 text="Double click on location to open new window.")
        self.species_instruction.grid(row=6, column=0, padx=5, pady=2)

        self.speciesList.bind('<Double-1>', self.get_species)

    def get_species(self, event):
        index = self.speciesList.curselection()
        label = self.speciesList.get(index)
        self.selected_species(label)

    def selected_species(self, name):
        species_name = name

        self.root_species = tkinter.Tk()
        self.root_species.wm_title(species_name)

        # Right BottomFrame - Select Species & Select Species Graph
        self.dataFrame = tkinter.LabelFrame(self.root_species, text="Add Data/Graphing")
        self.dataFrame.grid(row=0, column=15, columnspan=15, sticky="NW",
                            rowspan=10, padx=5, pady=5, ipadx=25, ipady=50)

        self.add_data_btn = tkinter.Button(self.dataFrame, text="Add Species Data",
                                           command=self.adding_species_data)
        self.add_data_btn.grid(row=2, column=16, sticky='W', padx=5, pady=2)

        self.graphing_btn = tkinter.Button(self.dataFrame, text="View Species Graphing",
                                           command=self.graphing)
        self.graphing_btn.grid(row=4, column=16, sticky='W', padx=5, pady=2)









# **************************************************************************************
#
#*****************************add_location_btn_function **********************************
#
#***************************************************************************************
    def adding_location(self):
        location_name = self.location_name_entry.get()

        self.locationList.insert("end", location_name)

        location_list.append(location_name)

        name_size = len(location_name)

        self.location_name_entry.delete(0, name_size)








#*********************************************************************************************
#
#******************************select_location_btn_function************************************
#
#*********************************************************************************************
    def add_species_name(self):
        self.root_add_species_name = tkinter.Tk()
        self.root_add_species_name.wm_title("Add Species Name Into Database")

        self.instruction_add_name = tkinter.LabelFrame(self.root_add_species_name, text="Adding Species Name")
        self.instruction_add_name.grid(row=0, columnspan=20, sticky='NW',
                                           rowspan=10, padx=5, pady=5, ipadx=10, ipady=4)

        # Create Label for Species Name
        self.label_species_name = tkinter.Label(self.instruction_add_name, text='Enter Species Name: ')
        self.label_species_name.grid(row=0, column=0)

        self.species_name_entry = tkinter.Entry(self.instruction_add_name, width=20)
        self.species_name_entry.grid(row=0, column=2, sticky='W')

        # Buttons
        self.add_name_button = tkinter.Button(self.instruction_add_name, text='Add Name',
                                              command=self.adding_name)
        self.add_name_button.grid(row=1, column=0, sticky='E', padx=5, pady=2)

        self.save_name_button = tkinter.Button(self.instruction_add_name, text='Save & Quit',
                                               command=self.root_add_species_name.destroy)
        self.save_name_button.grid(row=1, column=2, sticky='W', padx=5, pady=2)

    def adding_name(self):

        if not self.species_name_entry.get():
            species_name = 'N/A'
        else:
            species_name = self.species_name_entry.get()

        self.speciesList.insert("end", species_name)

        species_list.append(species_name)

        num_name = len(species_name)

        self.species_name_entry.delete(0, num_name)

    def delete_species_name(self):
        items = self.speciesList.curselection()
        pos = 0
        for i in items:
            idx = int(i) - pos
            self.speciesList.delete(idx, idx)
            pos = pos + 1

    def adding_species_data(self):
        self.root_add_species_data = tkinter.Tk()
        self.root_add_species_data.wm_title("Add Species Data Into Database")

        self.instruction_add_data = tkinter.LabelFrame(self.root_add_species_data, text="Adding Species Data")
        self.instruction_add_data.grid(row=0, columnspan=20, sticky='NW',
                                       rowspan=10, padx=5, pady=5, ipadx=10, ipady=4)

        # Create Label
        self.label_date = tkinter.Label(self.instruction_add_data, text='Enter Date: ')
        self.label_date.grid(row=0, column=0)

        self.date_entry = tkinter.Entry(self.instruction_add_data, width=15)
        self.date_entry.grid(row=0, column=2, sticky='W')

        self.label_population_size = tkinter.Label(self.instruction_add_data, text='Enter Population Size: ')
        self.label_population_size.grid(row=1, column=0)

        self.population_size_entry = tkinter.Entry(self.instruction_add_data, width=15)
        self.population_size_entry.grid(row=1, column=2, sticky='W')

        self.label_temperature = tkinter.Label(self.instruction_add_data, text='Enter Temperature by Ferenheight: ')
        self.label_temperature.grid(row=2, column=0)

        self.temperature_entry = tkinter.Entry(self.instruction_add_data, width=15)
        self.temperature_entry.grid(row=2, column=2, sticky='W')

        # Create button widgets for bottom frame
        self.add_data_button = tkinter.Button(self.instruction_add_data, text='Add Data',
                                              command=self.add_data)
        self.add_data_button.grid(row=3, column=0, sticky='E', padx=5, pady=2)

        self.save_data_button = tkinter.Button(self.instruction_add_data, text='Save & Quit',
                                               command=self.root_add_species_data.destroy)
        self.save_data_button.grid(row=3, column=0, sticky='W', padx=5, pady=2)

    def add_data(self):
        date = self.date_entry.get()
        population_size = self.population_size_entry.get()
        temperature = self.temperature_entry.get()

        date_list.append(date)
        population_list.append(population_size)
        temperature_list.append(temperature)

        date_size = len(date)
        population_length = len(population_size)
        temperature_size = len(temperature)

        self.date_entry.delete(0, date_size)
        self.population_size_entry.delete(0, population_length)
        self.temperature_entry.delete(0, temperature_size)

    def graphing(self):
        self.root_graphing = tkinter.Tk()
        self.root_graphing.wm_title("Graphing")

        plt.plot([1, 2, 3, 4])
        plt.ylabel('some numbers')
        plt.show()


my_gui = MyGUI()
