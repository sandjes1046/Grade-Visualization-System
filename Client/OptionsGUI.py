import tkinter as tk
from tkinter import ttk 
import tkinter.messagebox as msb
from tkinter import *


class Options():
    
    
        
        
        
    def on_closing(self):
        self.window.destroy()
        
        
        
    def set_per(self):
        self.info = "set percent"
        self.close()
        
    def close(self):
        self.window.destroy()
        
        
    def check_grades(self):
        self.info = "check grades"
        self.close()
        
    def check_average(self):
        self.info = "check average"
        self.close()
        
    def edit_grades(self):
        self.info = "edit grades"
        self.close()
        
    def class_stats(self):
        self.info = "stats"
        self.close()
        
    def go_back(self):
        self.info = "go back"
        self.close()
    
    def get_info(self):
        return(self.info)
        
    def __init__(self,role):
        self.window = tk.Tk()
        self.window.geometry("750x500+350+150")
        self.window.title('GVS')
        self.window.resizable(0,0)
        self.window.protocol("WM_DELETE_WINDOW", self.go_back)
        self.window.configure(bg = "white")

        self.role = role
        
        self.canvas = Canvas(self.window, bg = "white")
        self.titlecanvas = Canvas(self.window, bg = "orange")
        self.label = Label(self.titlecanvas, text = "Grade Visualization System", font = ('Arial',45), bg = 'orange')
        self.label.pack(side = LEFT)
        self.go_back = Button(self.titlecanvas, text = 'Back',width = 4, command = self.go_back)
        self.go_back.place(x = 710,y=0)
        
        self.buttonframe = Frame(self.canvas, bg = 'white')
        self.tag = Label(self.buttonframe, text = 'OPTIONS: ',bg = 'white')
        self.tag.grid(column = 0, row = 0)
        if(self.role == "student"):
            self.grades = Button(self.buttonframe, text = "Check Grades", command = self.check_grades)
            self.grades.grid(column=0,row=1)
            self.check_avg = Button(self.buttonframe, text = "Check Current Average", command = self.check_average)
            self.check_avg.grid(column = 1, row=1)
            self.class_stats = Button(self.buttonframe, text = "Class Statistics", command = self.class_stats)
            self.class_stats.grid(column = 2, row =1)
            
        if(self.role == "teacher"):
            self.grades = Button(self.buttonframe, text = "Edit Grades" ,command = self.edit_grades)
            self.set_avg = Button(self.buttonframe, text = "Set Percentages",command = self.set_per)
            self.class_stats = Button(self.buttonframe, text = "Class Statistics", command = self.class_stats)
            self.grades.grid(column =0,row=1)
            self.set_avg.grid(column=1,row=1)
            self.class_stats.grid(column = 2, row =1)
        
        
        
        self.buttonframe.pack()
        self.titlecanvas.pack(side = TOP, fill = 'both', expand = True)
        self.canvas.pack(side = BOTTOM, fill = 'both', expand = True)
        self.window.mainloop()
        
if __name__ == "__main__":
            Options("teacher") 
else:
        print("Code is being imported into another module") 