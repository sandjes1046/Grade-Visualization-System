# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 16:11:19 2021

@author: Sandjes1046
"""
import tkinter as tk
from tkinter import *
from tkinter import ttk
class Excel():
    
    
    def get_info(self):
        return self.saving
    
    
    def addAssignment(self):
        
        self.grades = []
        for i in range(self.num_of_rows):
            if( i == 0):#get header where it belongs
                entry = Entry(self.excel_frame, relief = SUNKEN, bd = 2)
                entry.grid(column = self.head_size, row = i)
                self.header_entries.append(entry)
            else:
                
                entry = Entry(self.excel_frame, relief = SUNKEN, bd = 2)
                entry.grid(column = self.head_size, row = i)
                self.grades.append(entry)
                
        self.overall_grades.append(self.grades)
        self.head_size += 1

        self.window.update()
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def save(self):
        
        self.saving = {}#dictionary
        
        final_grade = []
        final_overall_grade = []
        
        #loop to get the text
        for i in range(self.head_size):
            for j in range (self.num_of_students):
                if(i ==0 or i == 1):
                    final_grade.append(self.overall_grades[i][j].cget('text'))
                else:
                   final_grade.append(self.overall_grades[i][j].get()) 
            final_overall_grade.append(final_grade)
            final_grade = []
        
        for i in range(self.head_size):
        
            if(i == 0 or i == 1):#if they are labels, must use cget() function
                self.saving[f"{self.header_entries[i].cget('text')}"] = final_overall_grade[i]
            else:#if they are entry boxes
                self.saving[f"{self.header_entries[i].get()}"] = final_overall_grade[i]
        #print(self.saving)
        self.close()      
                
    
    def close(self):
        self.window.destroy()
    
    def on_closing(self):
        self.window.destroy()
    
    def __init__(self,headers,column_data):
        # get the size of headers and # of students
        self.head_size = len(headers)
        # we will always know that the first 2 columns will be student name and id
        self.num_of_students = len(column_data[0])
        
        self.num_of_rows = self.num_of_students + 1 #plus the header row
        
        
        self.window = tk.Tk()
        self.window.geometry("750x500+350+150")
        self.window.protocol("WM_DELETE_WINDOW", self.save)
        self.window.configure(bg = "white")
        
        self.main_frame = Frame(self.window)
        self.main_frame.pack(fill=BOTH,expand = True)
        
        self.canvas = Canvas(self.main_frame,bg = "orange", bd = 0, relief = 'ridge',highlightthickness=0)
        
        my_scb = ttk.Scrollbar(self.main_frame, orient='horizontal',
                       command=self.canvas.xview)

        my_scb.pack(side=BOTTOM,fill=X)
        self.canvas.pack(side = LEFT, fill=BOTH,expand=True)

        self.canvas.configure(xscrollcommand=my_scb.set)
        self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        
        self.excel_frame = Frame(self.canvas,bg = 'orange') 
        self.canvas.create_window((0,0), window=self.excel_frame,anchor="nw")

        
        
        self.button_frame = Frame(self.canvas,bg = 'orange')#holds all our buttons
        
         #make buttons
        self.saveIT = Button(self.button_frame, text = 'Save', command = self.save)
        self.saveIT.pack()
        self.assign_button = Button(self.button_frame, text = 'Add Assignment', command = self.addAssignment)
        self.assign_button.pack()
        
        #array stores all header entries
        self.header_entries = []
        for i in range(self.head_size):
            #if the header names are ID and Name, make them labels instead so the teacher cannot edit
            if( i == 0 or i == 1):
                self.label = Label(self.excel_frame,bg = 'white',width = 7,
                                   relief = SUNKEN,bd = 2,text = f"{headers[i]}")
                self.label.grid(column = i,row = 0)
                self.header_entries.append(self.label)
            else:
                self.entry = Entry(self.excel_frame,relief = SUNKEN, bd = 2)
                self.entry.insert(0,f"{headers[i]}")
                self.entry.grid(column = i,row = 0)
                self.header_entries.append(self.entry)
                
                
        #array stores grade data entries
        #need 2 arrays to make a list of lists
        self.grades = []
        self.overall_grades = []
        
        for i in range(self.head_size):
            for j in range(self.num_of_students):
                
                #if the header names are ID and Name, make them labels instead so the teacher cannot edit
                if( i == 0 or i == 1):
                    self.label = Label(self.excel_frame,bg = 'white',width = 7,relief = SUNKEN,bd = 2,text = f"{column_data[i][str(j)]}")
                    self.label.grid(column = i,row = j+1)# we add +1 to start below headers
                    self.grades.append(self.label)
                else:
                    self.entry = Entry(self.excel_frame,relief = SUNKEN, bd = 2)
                    self.entry.insert(0,f"{column_data[i][str(j)]}")
                    self.entry.grid(column = i,row = j+1)
                    self.grades.append(self.entry)
                
            self.overall_grades.append(self.grades)
            self.grades = []# reset list but do not use clear() on it
                
                
        #use the cget() function only for the first 2 columns

    
        #self.excel_frame.pack()
        self.button_frame.pack(side=BOTTOM)
        self.window.mainloop()


if __name__ == "__main__":
            Excel(['Name','ID','Assignment 1','Assignemnt 2'],[['john','michael','paul','rick'],['1234','4567','1478','20387136'],
                                               ['80','90','100','100'],['100','100','100','100']]) 
else:
        print("Code is being imported into another module") 