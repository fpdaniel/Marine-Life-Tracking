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
        self.useLocations.grid(row=0, column=15, columnspan=15, sticky='NE', rowspan=10, padx=5, pady=5,
                               ipadx=10, ipady=80)

        self.add_location_btn = tkinter.Button(self.useLocations, text="Add Location",
                                               command=self.add_location)
        self.add_location_btn.grid(row=2, column=5, sticky='W', padx=5, pady=2)

        self.delete_location_btn = tkinter.Button(self.useLocations, text="Delete Location",
                                                  command=self.delete_location)
        self.delete_location_btn.grid(row=4, column=5, padx=5, pady=2)

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
        self.top_frame = tkinter.Frame(self.root_add_location)
        self.mid_frame = tkinter.Frame(self.root_add_location)
        self.bottom_frame = tkinter.Frame(self.root_add_location)

        # Create Label for Species Name
        self.label_name = tkinter.Label(self.top_frame, text='Enter Location Name: ')
        self.location_name_entry = tkinter.Entry(self.top_frame, width=15)

        # Create pack and side for Label name
        self.label_name.pack(side='left')
        self.location_name_entry.pack(side='left')

        # Create button widgets for bottom frame
        self.add_location_button = tkinter.Button(self.bottom_frame, text='Add Location',
                                                  command=self.adding_location)
        self.save_button = tkinter.Button(self.bottom_frame, text='Save & Quit',
                                          command=self.root_add_location.destroy)

        # Pack buttons
        self.add_location_button.pack(side='left')
        self.save_button.pack(side='left')

        # Pack Frames
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

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
        self.speciesList.insert("end", species_list)
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

        self.add_data_btn = tkinter.Button(self.dataFrame, text="Select Species Data",
                                           command=self.adding_species_data)
        self.add_data_btn.grid(row=2, column=16, sticky='W', padx=5, pady=2)

        self.graphing_btn = tkinter.Button(self.dataFrame, text="Select Species Graphing",
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

        # Create frames
        self.top_frame_name = tkinter.Frame(self.root_add_species_name)
        self.bottom_frame_name = tkinter.Frame(self.root_add_species_name)

        # Create Label for Species Name
        self.label_species_name = tkinter.Label(self.top_frame_name, text='Enter Species Name: ')
        self.species_name_entry = tkinter.Entry(self.top_frame_name, width=15)

        # Create pack and side for Label name
        self.label_species_name.pack(side='left')
        self.species_name_entry.pack(side='left')

        # Buttons
        self.add_name_button = tkinter.Button(self.bottom_frame_name, text='Add Name',
                                              command=self.adding_name)
        self.save_name_button = tkinter.Button(self.bottom_frame_name, text='Save & Quit',
                                               command=self.root_add_species_name.destroy)

        # Pack buttons
        self.add_name_button.pack(side='left')
        self.save_name_button.pack(side='left')

        # Pack for frames
        self.top_frame_name.pack()
        self.bottom_frame_name.pack()

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

        # Create frames
        self.top_frame2 = tkinter.Frame(self.root_add_species_data)
        self.mid_frame2 = tkinter.Frame(self.root_add_species_data)
        self.bottom_frame2 = tkinter.Frame(self.root_add_species_data)
        self.last_frame2 = tkinter.Frame(self.root_add_species_data)

        # Create Label
        self.label_date = tkinter.Label(self.top_frame2, text='Enter Date: ')
        self.date_entry = tkinter.Entry(self.top_frame2, width=15)

        self.label_population_size = tkinter.Label(self.mid_frame2, text='Enter Population Size: ')
        self.population_size_entry = tkinter.Entry(self.mid_frame2, width=15)

        self.label_temperature = tkinter.Label(self.bottom_frame2, text='Enter Temperature by Ferenheight: ')
        self.temperature_entry = tkinter.Entry(self.bottom_frame2, width=15)

        # Create pack and side
        self.label_date.pack(side='left')
        self.date_entry.pack(side='left')

        self.label_population_size.pack(side='left')
        self.population_size_entry.pack(side='left')

        self.label_temperature.pack(side='left')
        self.temperature_entry.pack(side='left')

        # Create button widgets for bottom frame
        self.add_data_button = tkinter.Button(self.last_frame2, text='Add Data',
                                              command=self.add_data)
        self.save_data_button = tkinter.Button(self.last_frame2, text='Save & Quit',
                                               command=self.root_add_species_data.destroy)

        # Pack buttons
        self.add_data_button.pack(side='left')
        self.save_data_button.pack(side='left')

        # Pack Frames
        self.top_frame2.pack()
        self.mid_frame2.pack()
        self.bottom_frame2.pack()
        self.last_frame2.pack()

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
