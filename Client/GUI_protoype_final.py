# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 23:38:59 2021

@author: lolop
"""

import tkinter as tk


app = tk.Tk()

class Excel(tk.Frame):
    

    def __init__(self, master, rows, columns, width):
        super().__init__(master)

        for i in range(columns):
            self.make_entry(0, i+1, width, f'{i}', False) 

        for row in range(rows):
            self.make_entry(row+1, 0, 5, f'Name{row}', False)
                
            for column in range(columns):
                self.make_entry(row+1, column+1, width, '', True)



    def make_entry(self, row, column, width, text, state):
        e = tk.Entry(self, width=width)
        if text: e.insert(0, text)
        e['state'] = tk.NORMAL if state else tk.DISABLED
        e.coords = (row-1, column-1)
        e.grid(row=row, column=column)

ex = Excel(app, rows=5, columns=5, width=8)
ex.pack(padx=20, pady=20)


def show_cells():
    print('\n--== Saving ==--')
    for e in ex.children:
        v = ex.children[e]
        print(f'{v.get()}', end=', ')
    print()
    
def make_Columns():
    print('making columns')
    ex = Excel(app, rows=0, columns=+1, width=8) #this adds a column but on the bottom
    ex.pack(padx=0, pady=0)
   
bt = tk.Button(app, text='Save', command=show_cells)
bt.pack(pady=20)

bt = tk.Button(app, text='Add column', command=make_Columns)
bt.pack(pady=25)

app.mainloop()