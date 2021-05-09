import tkinter as tk
from tkinter import ttk 
import tkinter.messagebox as msb
from tkinter import *
from time import sleep

class Set_Percent():
    
    def get_info(self):
        if not self.percentages:
            self.percentages = [0,0,0]
            return(self.percentages)
        else:
            return(self.percentages)
    
    def on_closing(self):
        self.window.destroy()
        
        
    def close(self):
        self.window.destroy()
        
        
    def save(self):
        self.saved.configure(text = " ")
        self.window.update()
        assign = self.entry_assign.get()
        quiz = self.entry_quiz.get()
        test = self.entry_test.get()
        self.percentages = [assign,quiz,test]
        sleep(1)
        self.saved.configure(text = "Saved!",fg = 'green',font = ("bold", 10))
        
        self.window.update()
        
    def __init__(self):
        
        self.window = tk.Tk()
        self.window.geometry("750x500+350+150")
        self.window.title('GVS')
        self.window.resizable(0,0)
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.window.configure(bg = "white")
        self.window.resizable(0,0)
        self.percentages =[]
        
        self.canvas = Canvas(self.window, bg = "white", bd = 0, relief = 'ridge',highlightthickness=0)
        
        
        
      
        
        
       
        self.tinyframe = Frame(self.canvas, bg = 'white')
        self.label_assign = Label(self.tinyframe, text = 'Assignemnt %',bg = 'white')
        self.label_quiz = Label(self.tinyframe, text = 'Quiz %',bg = 'white')
        self.label_test = Label(self.tinyframe, text = 'Test %',bg = 'white')
        self.label_assign.grid(column = 1, row = 0)
        self.label_quiz.grid(column = 2, row = 0)
        self.label_test.grid(column = 3, row = 0)
        
        self.entry_assign = Entry(self.tinyframe,bd = 1,relief = 'solid')
        self.entry_quiz = Entry(self.tinyframe,bd = 1,relief = 'solid')
        self.entry_test = Entry(self.tinyframe,bd = 1,relief = 'solid')
        self.entry_assign.grid(column = 1, row = 1)
        self.entry_quiz.grid(column = 2, row = 1)
        self.entry_test.grid(column = 3, row = 1)
        
        self.grades = Button(self.tinyframe, text = "Save", bd = 1,relief = 'solid', width = 10, command = self.save)
        self.grades.grid(column = 2, row = 2)
        
        self.saved = Label(self.tinyframe, bg = 'white')
        self.saved.grid(column = 4, row = 1)
        
        
        self.tinyframe.place(x = 190,y=160)
        self.canvas.pack(side = BOTTOM, fill = 'both', expand = True)
        self.window.mainloop()
        
if __name__ == "__main__":
            Set_Percent() 
else:
        print("Code is being imported into another module") 