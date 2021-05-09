import numpy as np
import matplotlib.pyplot as plt
from tkinter import * 
from matplotlib.ticker import MaxNLocator#forces only whole numbers
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
from functools import partial

class Graph_It:
    
    def on_closing(self):
        self.window.destroy()
    
    def close(self):
        self.win.destroy()
    
    def stats(self):
        self.dataframe.destroy()
        self.dataframe = Frame(self.canvas, bg = 'white')
        
        self.countlabel = Label(self.dataframe, text = "Count",bg = 'white', font = ('Helvectica',10, 'bold'))
        self.countlabel.grid(column=0,row=1)
        self.maxlabel = Label(self.dataframe, text = "Max",bg = 'white', font = ('Helvectica',10, 'bold'))
        self.maxlabel.grid(column=0,row=2)
        self.minlabel = Label(self.dataframe, text = "Min",bg = 'white', font = ('Helvectica',10, 'bold'))
        self.minlabel.grid(column=0,row=3)
        self.meanlabel = Label(self.dataframe, text = "Mean",bg = 'white', font = ('Helvectica',10, 'bold'))
        self.meanlabel.grid(column=0,row=4)
        
        for i in range (len(self.assignments)):
            self.label = Label(self.dataframe, text = f"{self.assignments[i]}",bg = 'white', font = ('Helvectica',10, 'bold'))
            self.label.grid(column = i+1,row=0)
            
            
            
        for i in range(len(self.entire_data)):
            for j in range(len(self.entire_data[i])):
                self.info_label = Label(self.dataframe, text = f"{self.entire_data[i][j]}", width = 8,bg = 'white', borderwidth = 2, relief = 'solid')
                self.info_label.grid(column=j+1,row=i+1)
                
        self.dataframe.pack(side = TOP)
        
    
    def graph(self, num):
        
        #destroy to make room for new data
        self.dataframe.destroy()
        self.dataframe = Frame(self.canvas,bg = 'white')
        
        fig2 = plt.Figure(figsize=(6,8), dpi=155)
        ax = fig2.add_subplot(211)
        x = np.arange(len(self.grade_r[num]))
        ax.bar(x,self.grade_r[num],width=self.bar_width, color='blue')
        ax.set_title('Grade Distribution', y = 1.20)
        #ax.legend(loc="upper center", bbox_to_anchor=(0.5, 1.15), ncol=2,labels=['Class', 'Me'])
        ax.set_xlabel('Letter Grade', labelpad=5)
        ax.set_ylabel('Students')
        ax.set_xticks(x)
        ax.set_xticklabels(self.Letter_Grade, ha='left')
        ax.yaxis.set_major_locator(MaxNLocator(integer=True))#forces only whole numbers
        
        # Axis styling.
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.spines['bottom'].set_color('#DDDDDD')
        ax.tick_params(bottom=False, left=False)
        ax.set_axisbelow(True)
        ax.yaxis.grid(True, color='#EEEEEE')
        ax.xaxis.grid(False)
        
        graph = FigureCanvasTkAgg(fig2, master = self.dataframe)
        graph.get_tk_widget().pack(fill = 'both')
        self.dataframe.pack(side = TOP)
        
        
    def __init__(self,clas,mean,mins,maxs,counts,grds_rg,assign):
        
        self.means = mean
        self.mins = mins
        self.maxs = maxs
        self.count = counts
        self.grade_r = grds_rg
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
        
        
        
        
        
        
        
        buttonlist = Listbox(self.canvas)
        buttonlist.pack(side =TOP)
        
        self.main_stats = Button(buttonlist,text = "Class Stats",command = self.stats)
        self.main_stats.pack(side = LEFT)
        
        
        for i in range(len(self.assignments)):
            self.class_button = Button(buttonlist,text = f"{self.assignments[i]}",command = partial(self.graph,i))
            self.class_button.pack(side = LEFT)
        
                
        self.dataframe.pack(side = TOP)
        self.canvas.pack(fill = 'both', expand = True)
        self.window.mainloop()

if __name__ == "__main__":
            Graph_It("CSCI 0000",[48,56,90],[10,15,32],[40,56,89],[3,3,3],[[3,0,0,0,0],[2,0,0,0,1],[1,0,2,0,0]],["fake1","fake2","fake3"]) 
            #role,clas,mean,mins,maxs,counts,grds_rg,assign
else:
        print("Code is being imported into another module")    

















