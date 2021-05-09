# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 22:59:02 2021

@author: DanielSanchez
"""
import tkinter as tk
from tkinter import ttk 
import tkinter.messagebox as msb
from tkinter import *

class loginGUI:
    
    def redirectToSignUp(self):
        self.command = "sign up"
        self.win.destroy()
    
    def get_info(self):
        if(self.command == "sign up"):
            info = [f"{self.command}"]
            
        if(self.command == "exit GVS"):
            info = [f"{self.command}"]
            
        if(self.command == "log in"):
            if(self.v0.get() == 1):
                role = "teacher"
            if(self.v0.get() == 0):
                role = "student"
            info = [self.command,role, str(self.realemail),str(self.realpassword)]
        
        return(info)
    
    def close(self):
        self.win.destroy()
        
    def on_closing(self):
        if msb.askokcancel("Exit", "Do you really want to exit?"):
            self.command = "exit GVS"
            self.win.destroy()  
    
    def password_validate(self):
        password=self.password.get()
        self.realpassword = password.strip()
        
        self.submit_form()
    
    def submit_form(self):
        email=self.email.get()
        self.realemail = email.strip()
       
        self.command = "log in"
        print(f" Thanks for logging in {email}")
        
        self.win.destroy()
   
   
   
    def __init__(self): 
    
        self.win = tk.Tk()
        self.email  = tk.StringVar()
        self.password  = tk.StringVar()
        self.win.title("UTRGV Gradebook Visualization System(GVS)")
        w, h = self.win.winfo_screenwidth(), self.win.winfo_screenheight()
        self.win.geometry('400x400+525+250')
        self.win.configure(background = "orange");
        self.win.protocol("WM_DELETE_WINDOW", self.on_closing)  
        self.loginInfo = ttk.LabelFrame(self.win, text=' Login: ')
        self.loginInfo.grid(column=0, row=0,rowspan=10,columnspan=1, padx=10, pady=5,sticky='EWNS') 
        self.win.grid_rowconfigure(0, weight=0)
        self.win.grid_columnconfigure(0, weight=1)
        self.win.resizable(0,0)
        email_label = ttk.Label(self.loginInfo ,text = "Enter Email")
        self.email_entry = ttk.Entry(self.loginInfo, width=20, textvariable=self.email)
        
        email_label.grid(column=0, row=0, rowspan=1,columnspan=1,sticky='W')       
        self.email_entry.grid(column=1, row=0, rowspan=1,columnspan=1,sticky='W') 

        password_label = ttk.Label(self.loginInfo ,text = "Enter Password")
        self.password_entry = ttk.Entry(self.loginInfo, width=20, textvariable=self.password,show='*')
    
        password_label.grid(column=0, row=2, rowspan=1,columnspan=1,sticky='W')   
        self.password_entry.grid(column=1, row=2, rowspan=1,columnspan=1,sticky='W') 
   
        submit_button = ttk.Button(self.loginInfo, text = "Submit",  command=self.password_validate)   
        submit_button.grid(column=0, row=4,sticky='W')   
    
        signUp_button = ttk.Button(self.loginInfo, text = "Sign up!",  command=self.redirectToSignUp)   
        signUp_button.grid(column=1, row=4,sticky='W')   
        
        self.v0=IntVar()
        self.v0.set(0)
        r1=Radiobutton(self.loginInfo, text="Faculty", value=1, variable = self.v0)
        r1.grid(column = 2, row = 4)
        r2=Radiobutton(self.loginInfo, text="Student", value=0, variable = self.v0)
        r2.grid(column = 3, row = 4)
        
        self.win.mainloop()

if __name__ == "__main__":
            loginGUI() 
else:
        print("Code is being imported into another module")    



