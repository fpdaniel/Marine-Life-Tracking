import tkinter
import tkinter.messagebox

import numpy as np
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
        self.locationList.insert("end", location_list)
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

        self.select_location_btn = tkinter.Button(self.useLocations, text="Select Location",
                                                  command=self.select_location)
        self.select_location_btn.grid(row=6, column=5, padx=5, pady=2)



        #Enter tkinter loop
        tkinter.mainloop()

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


    def select_location(self):
        self.root_select = tkinter.Tk()
        self.root_select.wm_title("Select Location")

        #Left Frame - Species List
        self.leftFrame1 = tkinter.LabelFrame(self.root_select, text="Species List")
        self.leftFrame1.grid(row=0, columnspan=10, sticky='NW', rowspan=10, padx=5, pady=5, ipadx=0, ipady=70)

        self.scrollbar2 = tkinter.Scrollbar(self.leftFrame1)
        self.scrollbar2.pack(side="right", fill="y")

        self.speciesList = tkinter.Listbox(self.leftFrame1, yscrollcommand=self.scrollbar2.set)
        self.speciesList.insert("end", species_list)
        self.speciesList.pack(side="left", fill="y")
        self.scrollbar2.config(command=self.speciesList.yview)

        #Right TopFrame - Add Species, Delete Species
        self.speciesFrame = tkinter.LabelFrame(self.root_select, text="Add/Delete Species")
        self.speciesFrame.grid(row=0, column=15, columnspan=15, sticky='NW',
                               rowspan=10, padx=5, pady=5, ipadx=25, ipady=50)

        self.add_species_button = tkinter.Button(self.speciesFrame, text="Add Species",
                                                 command=self.add_species_name)
        self.add_species_button.grid(row=2, column=16, sticky='W', padx=5, pady=2)

        self.delete_species_button = tkinter.Button(self.speciesFrame, text="Delete Species",
                                                    command=self.delete_species_name)
        self.delete_species_button.grid(row=2, column=32, sticky='W', padx=5, pady=2)

        #Right BottomFrame - Select Species & Select Species Graph
        self.dataFrame = tkinter.LabelFrame(self.root_select, text="Add Data/Graphing")
        self.dataFrame.grid(row=12, column=15, columnspan=15, sticky="NW",
                            rowspan=10, padx=5, pady=5, ipadx=25, ipady=50)

        self.add_data_btn = tkinter.Button(self.dataFrame, text="Select Species Data",
                                           command=self.adding_species_data)
        self.add_data_btn.grid(row=2, column=16, sticky='W', padx=5, pady=2)

        self.graphing_btn = tkinter.Button(self.dataFrame, text="Select Species Graphing",
                                           command=self.graphing)
        self.graphing_btn.grid(row=4, column=16, sticky='W', padx=5, pady=2)


    def graphing(self):
        self.root_graphing = tkinter.Tk()
        self.root_graphing.wm_title("Graphing")

        plt.plot([1, 2, 3, 4])
        plt.ylabel('some numbers')
        plt.show()

        # evenly sampled time at 200ms intervals
        t = np.arange(0., 5., 0.2)

        # red dashes, blue squares and green triangles
        plt.plot(t, t, 'r--', t, t ** 2, 'bs', t, t ** 3, 'g^')
        plt.show()


    def adding_location(self):
        location_name = self.location_name_entry.get()

        location_list.append(location_name)

        name_size = len(location_name)

        self.location_name_entry.delete(0, name_size)

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

        #Buttons
        self.add_name_button = tkinter.Button(self.bottom_frame_name, text='Add Name',
                                                  command=self.adding_name)
        self.save_name_button = tkinter.Button(self.bottom_frame_name, text='Save & Quit',
                                          command=self.root_add_species_name.destroy)

        # Pack buttons
        self.add_name_button.pack(side='left')
        self.save_name_button.pack(side='left')

        #Pack for frames
        self.top_frame_name.pack()
        self.bottom_frame_name.pack()


    def adding_name(self):
        if not self.species_name_entry.get():
            species_name = 'N/A'
        else:
            species_name = self.species_name_entry.get()

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



my_gui = MyGUI()








# # Create frames
        # self.top_frame = tkinter.Frame(self.main_window)
        # self.mid_frame = tkinter.Frame(self.main_window)
        # self.bottom_frame = tkinter.Frame(self.main_window)
# #Create Label for Species Name
        # self.label_name = tkinter.Label(self.top_frame, text='Species Name: ')
        # self.name_entry = tkinter.Entry(self.top_frame, width=15)
        #
        # #Create pack and side for Label name
        # self.label_name.pack(side='left')
        # self.name_entry.pack(side='left')
        #
        # #Create Number Size for label number
        # self.label_number = tkinter.Label(self.mid_frame, text='Population Size: ')
        # self.size_entry = tkinter.Entry(self.mid_frame, width=10)
        #
        # #Create pack and side for Label Number
        # self.label_number.pack(side='left')
        # self.size_entry.pack(side='left')
        #
        # #Create button widgets for bottom frame
        # self.add_name_button = tkinter.Button(self.bottom_frame, text='Add Species data', command=self.adding)
        # self.save_button = tkinter.Button(self.bottom_frame, text='Save', command=self.main_window.destroy)
        #
        # #Pack buttons
        # self.add_name_button.pack(side='left')
        # self.save_button.pack(side='left')
        #
        # #Pack Frames
        # self.top_frame.pack()
        # self.mid_frame.pack()
        # self.bottom_frame.pack()









#Example
# if __name__ == '__main__':
#     form = tkinter.Tk()
#
#     getFld = tkinter.IntVar()
#
#     form.wm_title('File Parser')
#
#     stepOne = tkinter.LabelFrame(form, text=" 1. Enter File Details: ")
#     stepOne.grid(row=0, columnspan=7, sticky='W', \
#                  padx=5, pady=5, ipadx=5, ipady=5)
#
#     helpLf = tkinter.LabelFrame(form, text=" Quick Help ")
#     helpLf.grid(row=0, column=9, columnspan=2, rowspan=8, \
#                 sticky='NS', padx=5, pady=5)
#     helpLbl = tkinter.Label(helpLf, text="Help will come - ask for it.")
#     helpLbl.grid(row=0)
#
#     stepTwo = tkinter.LabelFrame(form, text=" 2. Enter Table Details: ")
#     stepTwo.grid(row=2, columnspan=7, sticky='W', \
#                  padx=5, pady=5, ipadx=5, ipady=5)
#
#     stepThree = tkinter.LabelFrame(form, text=" 3. Configure: ")
#     stepThree.grid(row=3, columnspan=7, sticky='W', \
#                    padx=5, pady=5, ipadx=5, ipady=5)
#
#     inFileLbl = tkinter.Label(stepOne, text="Select the File:")
#     inFileLbl.grid(row=0, column=0, sticky='E', padx=5, pady=2)
#
#     inFileTxt = tkinter.Entry(stepOne)
#     inFileTxt.grid(row=0, column=1, columnspan=7, sticky="WE", pady=3)
#
#     inFileBtn = tkinter.Button(stepOne, text="Browse ...")
#     inFileBtn.grid(row=0, column=8, sticky='W', padx=5, pady=2)
#
#     outFileLbl = tkinter.Label(stepOne, text="Save File to:")
#     outFileLbl.grid(row=1, column=0, sticky='E', padx=5, pady=2)
#
#     outFileTxt = tkinter.Entry(stepOne)
#     outFileTxt.grid(row=1, column=1, columnspan=7, sticky="WE", pady=2)
#
#     outFileBtn = tkinter.Button(stepOne, text="Browse ...")
#     outFileBtn.grid(row=1, column=8, sticky='W', padx=5, pady=2)
#
#     inEncLbl = tkinter.Label(stepOne, text="Input File Encoding:")
#     inEncLbl.grid(row=2, column=0, sticky='E', padx=5, pady=2)
#
#     inEncTxt = tkinter.Entry(stepOne)
#     inEncTxt.grid(row=2, column=1, sticky='E', pady=2)
#
#     outEncLbl = tkinter.Label(stepOne, text="Output File Encoding:")
#     outEncLbl.grid(row=2, column=5, padx=5, pady=2)
#
#     outEncTxt = tkinter.Entry(stepOne)
#     outEncTxt.grid(row=2, column=7, pady=2)
#
#     outTblLbl = tkinter.Label(stepTwo, \
#           text="Enter the name of the table to be used in the statements:")
#     outTblLbl.grid(row=3, column=0, sticky='W', padx=5, pady=2)
#
#     outTblTxt = tkinter.Entry(stepTwo)
#     outTblTxt.grid(row=3, column=1, columnspan=3, pady=2, sticky='WE')
#
#     fldLbl = tkinter.Label(stepTwo, \
#                            text="Enter the field (column) names of the table:")
#     fldLbl.grid(row=4, column=0, padx=5, pady=2, sticky='W')
#
#     getFldChk = tkinter.Checkbutton(stepTwo, \
#                            text="Get fields automatically from input file",\
#                            onvalue=1, offvalue=0)
#     getFldChk.grid(row=4, column=1, columnspan=3, pady=2, sticky='WE')
#
#     fldRowTxt = tkinter.Entry(stepTwo)
#     fldRowTxt.grid(row=5, columnspan=5, padx=5, pady=2, sticky='WE')
#
#     transChk = tkinter.Checkbutton(stepThree, \
#                text="Enable Transaction", onvalue=1, offvalue=0)
#     transChk.grid(row=6, sticky='W', padx=5, pady=2)
#
#     transRwLbl = tkinter.Label(stepThree, \
#                  text=" => Specify number of rows per transaction:")
#     transRwLbl.grid(row=6, column=2, columnspan=2, \
#                     sticky='W', padx=5, pady=2)
#
#     transRwTxt = tkinter.Entry(stepThree)
#     transRwTxt.grid(row=6, column=4, sticky='WE')
#
#     form.mainloop()
