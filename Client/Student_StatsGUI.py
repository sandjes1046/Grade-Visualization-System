import numpy as np
import matplotlib.pyplot as plt
from tkinter import * 
from matplotlib.ticker import MaxNLocator#forces only whole numbers
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
from functools import partial

class Table:
    
    def on_closing(self):
        self.window.destroy()
    
    def close(self):
        self.win.destroy()
    
    
        
        
    def __init__(self,clas,mean,mins,maxs,counts,assign):
        
        self.means = mean
        self.mins = mins
        self.maxs = maxs
        self.count = counts
        self.assignments = assign
        self.Letter_Grade = ['A','B','C','D','F']
        self.clas = clas
        self.entire_data = [self.count, self.maxs, self.mins, self.means]

        self.bar_width=0.25
        
        
        
        ################################################################
        self.window = Tk()
        self.window.title('Grade Display')
        self.window.configure(bg = "white")
        # dimensions of the main window
        self.window.geometry("1200x1000")
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)  
        #window.resizable(0,0)
        
        self.canvas = Canvas(self.window, bg = 'white', highlightthickness = 0)
        self.title = Frame(self.canvas,bg = 'white')
        self.title.pack()
        self.titlelabel = Label(self.title, text = f"{self.clas}", bg = 'white',font = ('bold'))
        self.titlelabel.pack(ipady = 10)
        
        self.dataframe = Frame(self.canvas,bg = 'white')
        
        self.countlabel = Label(self.dataframe, text = "Count", bg = 'white', font = ('Helvectica',10, 'bold'))
        self.countlabel.grid(column=0,row=1)
        self.maxlabel = Label(self.dataframe, text = "Max", bg = 'white', font = ('Helvectica',10, 'bold'))
        self.maxlabel.grid(column=0,row=2)
        self.minlabel = Label(self.dataframe, text = "Min", bg = 'white', font = ('Helvectica',10, 'bold'))
        self.minlabel.grid(column=0,row=3)
        self.meanlabel = Label(self.dataframe, text = "Mean", bg = 'white', font = ('Helvectica',10, 'bold'))
        self.meanlabel.grid(column=0,row=4)
        
        for i in range (len(self.assignments)):
            self.label = Label(self.dataframe, text = f"{self.assignments[i]}", bg = 'white', font = ('Helvectica',10, 'bold'))
            self.label.grid(column = i+1,row=0)
            
            
            
        for i in range(len(self.entire_data)):
            for j in range(len(self.entire_data[i])):
                self.info_label = Label(self.dataframe, text = f'{self.entire_data[i][j]}', width = 8,bg = 'white', borderwidth = 2, relief = 'solid')
                self.info_label.grid(column=j+1,row=i+1)
        
        
        
        
        
        
        
        
        
        
        
                
        self.dataframe.pack(side = TOP)
        self.canvas.pack(fill = 'both', expand = True)
        self.window.mainloop()

if __name__ == "__main__":
            Table("CSCI 0000",[48,56,90],[10,15,32],[40,56,89],[3,3,3],["fake1","fake2","fake3"]) 
            #clas,mean,mins,maxs,counts,assign
else:
        print("Code is being imported into another module")    

















