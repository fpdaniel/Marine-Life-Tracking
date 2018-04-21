import tkinter
import tkinter.messagebox

#import sqlite3

species_list = []
species_names = []


class MyGUI:
    def __init__(self):
        #Create main window widget
        self.main_window = tkinter.Tk()

        #Create frames
        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        #Create Label for Species Name
        self.label_name = tkinter.Label(self.top_frame, text='Species Name: ')
        self.name_entry = tkinter.Entry(self.top_frame, width=15)

        #Create pack and side for Label name
        self.label_name.pack(side='left')
        self.name_entry.pack(side='left')

        #Create Number Size for label number
        self.label_number = tkinter.Label(self.mid_frame, text='Population Size: ')
        self.size_entry = tkinter.Entry(self.mid_frame, width=10)

        #Create pack and side for Label Number
        self.label_number.pack(side='left')
        self.size_entry.pack(side='left')

        #Create button widgets for bottom frame
        self.add_name_button = tkinter.Button(self.bottom_frame, text='Add Species data', command=self.adding)
        self.save_button = tkinter.Button(self.bottom_frame, text='Save', command=self.main_window.destroy)

        #Pack buttons
        self.add_name_button.pack(side='left')
        self.save_button.pack(side='left')

        #Pack Frames
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        #Enter tkinter loop
        tkinter.mainloop()

        print(species_list)


    def adding(self):
        species_data = {}

        if not self.name_entry.get():
            species_name = 'N/A'
        else:
            species_name = self.name_entry.get()

        if not self.size_entry.get():
            population_size = 'N/A'
        else:
            population_size = self.size_entry.get()

        species_data[species_name] = population_size
        species_list.append(species_data)

        num_name = len(species_name)
        num_size = len(population_size)

        self.name_entry.delete(0, num_name)
        self.size_entry.delete(0, num_size)

my_gui = MyGUI()

import numpy as np
import matplotlib.pyplot as plt
plt.plot([1,2,3,4])
plt.ylabel('some numbers')
plt.show()

# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()