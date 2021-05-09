import tkinter as tk
from tkinter import ttk 
import tkinter.messagebox as msb
from tkinter import *
from functools import partial


class Mainpage():
    
    def get_info(self):
        return(self.selected)
    
    def log_out(self):
        self.selected = "log out"
        self.close()
        
    def SelectClass(self,x):
        self.selected = self.user_classes[x]
        print(x)
        print(self.user_classes[x])
        self.close()
        
    def close(self):
        self.window.destroy()
        
    def on_closing(self):
        if msb.askokcancel("Exit", "Do you really want to log out?"):
            self.selected = "log out"
            self.window.destroy()
    
    def __init__(self,user_classes):
        self.window = tk.Tk()
        self.window.geometry("750x500+350+150")
        self.window.title('GVS')
        self.window.resizable(0,0)
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.window.configure(bg = "white")
       
        self.canvasbottom = Canvas(self.window)
        s = ttk.Style()
        s.configure('Red.TLabelframe.Label', background='white')
        self.classframe = ttk.LabelFrame(self.canvasbottom, text = " Classes: ", style = 'Red.TLabelframe.Label')
        
        self.class_len = len(user_classes)
        self.user_classes = user_classes
        if(self.user_classes[0] == "No Class"):
            for i in range(self.class_len):
                self.class_button = Button(self.classframe, text=f"{user_classes[i]}",state = DISABLED)
                self.class_button.grid(column = i, row = 0)
        else:
            for i in range(self.class_len):
                self.class_button = Button(self.classframe, text=f"{user_classes[i]}",command = partial(self.SelectClass,i))
                self.class_button.grid(column = i, row = 0)
                
        self.titleframe = tk.Frame(self.window, bg = 'orange')
        self.titleframe.config(background = 'orange')
        self.logout = Button(self.titleframe, text = "Log out",command = self.log_out)
        self.logout.place(x = 700,y=0)
        self.label = Label(self.titleframe, text = "Grade Visualization System", font = ('Arial',45), bg = 'orange')
        self.label.pack(side = LEFT)
        
        
        
        self.titleframe.pack(side = TOP,fill = 'both',expand = True)
        self.classframe.pack(side = BOTTOM,fill = 'both', expand = True)
        self.canvasbottom.pack(side = BOTTOM,expand = True)
        
        self.window.mainloop()
if __name__ == "__main__":
            Mainpage(["No Class","No Class"]) 
else:
        print("Code is being imported into another module")          
        