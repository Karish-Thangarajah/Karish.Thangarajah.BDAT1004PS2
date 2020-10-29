# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 23:44:01 2020

@author: karis
"""

from tkinter import *

class Mortgage(Frame):
    
    def __init__(self, master):
        Frame.__init__(self, master)
        label = Label(self, text='Loan Amount:')
        label.grid(row=0, column=0)
        loanAmEnt = Entry(self)
        loanAmEnt.grid(row=0, column=1)
        
        label = Label(self, text='Interest Rate:')
        label.grid(row=1, column=0)
        intRateEnt = Entry(self)
        intRateEnt.grid(row=1, column=1)
        
        label = Label(self, text='Loan Terms:')
        label.grid(row=2, column=0)
        loanTeEnt = Entry(self)
        loanTeEnt.grid(row=2, column=1)
            
        button = Button(self, text='Compute mortgage', command=self.compute)
        button.grid(row=3, column=0)
        AnsEnt = Entry(self)
        AnsEnt.grid(row=3,column=1)
        
    def compute(self):
        return None
    

root = Tk()
app = Mortgage(root)
app.pack()
root.mainloop()




