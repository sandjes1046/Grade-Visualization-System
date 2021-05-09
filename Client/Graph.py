import numpy as np
import matplotlib.pyplot as plt
from tkinter import * 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)

class Graph:
    
    def on_closing(self):
        self.window.destroy()
    
    def close(self):
        self.win.destroy()
        
        
    def __init__(self, avg, gd, asmts):
#these lists are obtained from the server
        averages = avg
        grades = gd
        assessments = asmts
        #this code generates the graphs################################################
        bar_width=0.35
        
        fig2 = plt.Figure(figsize=(6,8), dpi=155)
        ax = fig2.add_subplot(211)
        x = np.arange(len(assessments))
        ax.bar(x,averages,width=bar_width,color='silver')
        ax.bar(x+bar_width,grades,width=bar_width, color='darkorange')
        ax.set_title('Class Average/Student Grades', y = 1.20)
        ax.legend(loc="upper center", bbox_to_anchor=(0.5, 1.15), ncol=2,labels=['Class', 'Me'])
        ax.set_xlabel('Assessment', labelpad=5)
        ax.set_ylabel('Score/100')
        ax.set_xticks(x+bar_width / 2)
        ax.set_xticklabels(assessments, rotation=90, ha='left')
        
        # Axis styling.
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.spines['bottom'].set_color('#DDDDDD')
        ax.tick_params(bottom=False, left=False)
        ax.set_axisbelow(True)
        ax.yaxis.grid(True, color='#EEEEEE')
        ax.xaxis.grid(False)
                
        
        ################################################################
        self.window = Tk()
        self.window.title('Grade Display')
        self.window.configure(bg = "white")
        # dimensions of the main window
        self.window.geometry("1200x1000")
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)  
        #window.resizable(0,0)
        
        subcanvas = Canvas(self.window, bg = "white", height = 500, width = 0)
        canvasgraph = FigureCanvasTkAgg(fig2, master = subcanvas)#shows the graphs
        canvasgraph.get_tk_widget().pack(fill = 'both')
        
        subcanvas.pack(side = LEFT)
        
        textcanvas = Canvas(self.window, bg = "white" ,highlightbackground = "white")
        theirlabel = Label(textcanvas, bg ="white" ,border = 1, text = "Your Grades:", 
                           font = ("times new roman", 12, "underline"))
        theirlabel.pack()
  
        myList = Listbox(textcanvas)
        myList.pack()
        
        for i in range(len(assessments)):
            mylabel = Label(myList, bg ="white" ,text = f"{assessments[0+i]} - {grades[0+i]}  ",
                            font = ("times new roman", 12))
            mylabel.pack()
        
        
        textcanvas.pack(side = LEFT, fill = Y)
        
        
        self.window.mainloop()

if __name__ == "__main__":
            Graph([100,100,100],[100,100,100],["fake","fake","fake"]) 
else:
        print("Code is being imported into another module")    

















