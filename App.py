# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 00:34:17 2020

@author: karis
"""

import sys
sys.path.insert(1, '/Users/karis/OneDrive/Desktop/BDAT1004')

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

class Calculator(Frame):
    labels = [['MC','M+','M-','MR'],
              ['C','\u221A', 'x^2', '+'],
              ['7','8','9','-'],
              ['4','5','6','*'],
              ['1','2','3','/'],
              ['0','.','+-','=']]
    
    def __init__(self, master):
        Frame.__init__(self, master)
        DisplayEnt = Entry(self)
        DisplayEnt.grid(row=0, column=0, columnspan=4, )
        
        for r in range(1,7):
            for c in range(4):
                label = Button(self, relief=RAISED, 
                              width=5,height=1,
                              text=self.labels[r-1][c])
                label.grid(row=r,column=c)
                
class App(Frame):
    
    def __init__(self, master):
        Frame.__init__(self, master)
        mortgage = Mortgage(self)
        mortgage.pack(side=LEFT)
        calculator = Calculator(self)
        calculator.pack(side=RIGHT)
        
root = Tk()
app = App(root)
app.pack()
root.mainloop()