import tkinter.messagebox as msb
from tkinter import *
from tkinter import ttk
import tkinter as tk


class Error:
    
    
    def on_closing(self):
        self.root.destroy()
    
    def __init__(self,flag):
        self.root = tk.Tk()
        self.root.geometry('200x100+700+350')
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.configure(bg = "white")
        self.root.resizable(0,0)
        if(flag == 0):
            self.root.title("ERROR")
            label = Label(self.root,text="Record already exists",bg ="white")
            label.pack(side = TOP, fill = "both", expand = True)

        if(flag == 1):
            self.root.title("SUCCESS")
            label = Label(self.root,text="Record added successfully",bg ="white")
            label.pack()
        if(flag == 2):
            self.root.title("ERROR")
            label = Label(self.root,text="Record doesn't exist, go signup",bg ="white")
            label.pack()
        if(flag == 3):
            self.root.title("ERROR")
            label = Label(self.root,text="Password incorrect, try again",bg ="white")
            label.pack()
        if(flag == 4):
            self.root.title("ERROR")
            label = Label(self.root,text="No classes found",bg ="white")
            label.pack()
        if(flag == 5):
            self.root.title("SUCCESS")
            label = Label(self.root,text="Success!",bg ="white")
            label.pack()
            
        button = Button(self.root, text="OK", width = 10,command=lambda: self.root.destroy())
        button.pack(side="bottom", fill="none", expand=True) 
        self.root.mainloop()