# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 22:59:02 2021

@author: lolop
"""
import tkinter as tk
from tkinter import ttk 
import tkinter.messagebox as msb
from tkinter import *

class SignUpGUI:
    
    def get_info(self):
        if(self.command == "back to login"):
            info = [self.command]
        if(self.command == "sign up"):
            if(self.v0.get() == 1):
                role = "teacher"
            if(self.v0.get() == 0):
                role = "student"
            info = [self.command,role, str(self.realID),str(self.realemail),str(self.realpassword)]
        
        return(info)
    
    def close(self):
        self.win.destroy()
        
    def on_closing(self):
        if msb.askokcancel("Exit", "Do you really want to exit?"):
            self.command = "back to login"
            self.win.destroy()  
    
    def password_validate(self):
        password=self.password.get()
        self.realpassword = password.strip()
        
        Confirmpassword=self.Confirmpassword.get()
        self.realConfirmpassword = Confirmpassword.strip()
        
        if(self.realpassword != self.realConfirmpassword):
            msb.showinfo(title = "Error: Password", message = 
                         "Your passwords do not match, try again")
        if(self.realpassword == self.realConfirmpassword):
            self.submit_form()
            
    def email_validate(self):
        email=self.email.get()
        self.realemail = email.strip()
        
        x = self.realemail.endswith("@utrgv.edu")
        
        if(x == False):
            msb.showinfo(title = "Error: Email", message = 
                         "Your email is not a valid UTRGV email, try again")
        if(x == True):
            self.password_validate()
    
    def submit_form(self):
  
        ID=self.ID.get()
        self.realID = ID.strip()
        
       
        self.command = "sign up"
        print(f" Thanks for signing up! You entered {self.realemail} and {ID} and {self.realpassword}")
        
        self.close()
       
    def __init__(self): 
    
        self.win = tk.Tk()
        self.email  = tk.StringVar()
        self.ID  = tk.StringVar()
        self.password  = tk.StringVar()
        self.Confirmpassword  = tk.StringVar()
        self.win.title("UTRGV Gradebook Visualization System(GVS)")
        w, h = self.win.winfo_screenwidth(), self.win.winfo_screenheight()
        self.win.geometry('400x400+500+250')
        self.win.configure(background = "orange");
        self.win.resizable(0,0)
        self.win.protocol("WM_DELETE_WINDOW", self.on_closing)  
    
        self.signUpInfo = ttk.LabelFrame(self.win, text=' Sign Up: ')
        self.signUpInfo.grid(column=0, row=0,rowspan=10,columnspan=1, padx=10, pady=5,sticky='EWNS') 
    
        self.win.grid_rowconfigure(0, weight=0)
        self.win.grid_columnconfigure(0, weight=1)
    
        email_label = ttk.Label(self.signUpInfo ,text = "Enter Email")
        self.email_entry = ttk.Entry(self.signUpInfo, width=20, textvariable=self.email)
        
        email_label.grid(column=0, row=0, rowspan=1,columnspan=1,sticky='W')       
        self.email_entry.grid(column=1, row=0, rowspan=1,columnspan=1,sticky='W') 

        ID_label = ttk.Label(self.signUpInfo ,text = "Enter ID")
        self.ID_entry = ttk.Entry(self.signUpInfo, width=20, textvariable=self.ID)
    
        ID_label.grid(column=0, row=1, rowspan=1,columnspan=1,sticky='W')   
        self.ID_entry.grid(column=1, row=1, rowspan=1,columnspan=1,sticky='W') 
    
        password_label = ttk.Label(self.signUpInfo ,text = "Enter Password")
        self.password_entry = ttk.Entry(self.signUpInfo, width=20, textvariable=self.password,show='*')
    
        password_label.grid(column=0, row=2, rowspan=1,columnspan=1,sticky='W')   
        self.password_entry.grid(column=1, row=2, rowspan=1,columnspan=1,sticky='W') 
   
        Confirmpassword_label = ttk.Label(self.signUpInfo ,text = "Confirm Password")
        self.Confirmpassword_entry = ttk.Entry(self.signUpInfo, width=20, textvariable=self.Confirmpassword,show='*')

        Confirmpassword_label.grid(column=0, row=3, rowspan=1,columnspan=1,sticky='W')   
        self.Confirmpassword_entry.grid(column=1, row=3, rowspan=1,columnspan=1,sticky='W') 

        submit_button = ttk.Button(self.signUpInfo, text = "Submit",  command=self.email_validate)   
        submit_button.grid(column=0, row=4,sticky='W')   
        
        self.v0=IntVar()
        self.v0.set(0)
        r1=Radiobutton(self.signUpInfo, text="Faculty", value=1, variable = self.v0)
        r1.place(x=100,y=90)
        r2=Radiobutton(self.signUpInfo, text="Student", value=0, variable = self.v0)
        r2.place(x=200,y=90)
    
        self.signUpInfo.grid_rowconfigure(0, weight=1)
        self.signUpInfo.grid_rowconfigure(1, weight=1)
        self.signUpInfo.grid_rowconfigure(2, weight=1)
        self.signUpInfo.grid_rowconfigure(3, weight=1)
        
        self.signUpInfo.grid_columnconfigure(0, weight=0)
        self.signUpInfo.grid_columnconfigure(1, weight=0)
        
        self.win.mainloop()

if __name__ == "__main__":
    
            SignUpGUI() 
else:
        print("Code is being imported into another module")    



