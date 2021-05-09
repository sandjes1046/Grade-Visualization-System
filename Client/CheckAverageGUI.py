import tkinter as tk
from tkinter import ttk 
import tkinter.messagebox as msb
from tkinter import *


class Check_Average():
    
    
    def on_closing(self):
        self.window.destroy()
        
        
    def close(self):
        self.window.destroy()
        
        
    def check_average(self):
        total = (float(self.entry_assign.get()) * (float(self.percentages[0])/100)) + (float(self.entry_quiz.get()) * (float(self.percentages[1])/100)) + (float(self.entry_test.get()) * (float(self.percentages[2])/100))
        
        
        self.total.configure(text = f"= {total}")
        self.window.update()
        
    def __init__(self,percentages,grades,assignments):
        
        self.window = tk.Tk()
        self.window.geometry("750x500+350+150")
        self.window.title('GVS')
        self.window.resizable(0,0)
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.window.configure(bg = "white")
        self.window.resizable(0,0)
        self.percentages = percentages
        self.grades = grades
        self.assignments = assignments
        
        self.canvas = Canvas(self.window, bg = "white", bd = 0, relief = 'ridge',highlightthickness=0)
        
        
        
        myList = Listbox(self.canvas, relief = 'flat',highlightthickness = 0)
        myList.pack(side = LEFT, fill = Y)
        
        for i in range(len(self.assignments)):
            mylabel = Label(myList, bg ="white" ,text = f"{self.assignments[0+i]} - {self.grades[0+i]}  ",
                            font = ("times new roman", 12))
            mylabel.pack()
        
        
       
        self.tinyframe = Frame(self.canvas, bg = 'white')
        self.label_assign = Label(self.tinyframe, text = 'Assignemnts',bg = 'white')
        self.label_quiz = Label(self.tinyframe, text = 'Quizzes',bg = 'white')
        self.label_test = Label(self.tinyframe, text = 'Tests',bg = 'white')
        self.label_assign.grid(column = 1, row = 0)
        self.label_quiz.grid(column = 2, row = 0)
        self.label_test.grid(column = 3, row = 0)
        
        self.entry_assign = Entry(self.tinyframe,bd = 1,relief = 'solid')
        self.entry_quiz = Entry(self.tinyframe,bd = 1,relief = 'solid')
        self.entry_test = Entry(self.tinyframe,bd = 1,relief = 'solid')
        self.entry_assign.grid(column = 1, row = 1)
        self.entry_quiz.grid(column = 2, row = 1)
        self.entry_test.grid(column = 3, row = 1)
        
        self.grades = Button(self.tinyframe, text = "Check Average", bd = 1,relief = 'solid', command = self.check_average)
        self.grades.grid(column = 0, row = 1)
        
        self.total = Label(self.tinyframe, bg = 'white')
        self.total.grid(column = 4, row = 1)
        
        
        self.tinyframe.place(x = 165,y=160)
        self.canvas.pack(side = BOTTOM, fill = 'both', expand = True)
        self.window.mainloop()
        
if __name__ == "__main__":
            Check_Average([30,40,30],[0,0,0,0,0],['fake','fake','fake','fake','fake']) 
else:
        print("Code is being imported into another module") 