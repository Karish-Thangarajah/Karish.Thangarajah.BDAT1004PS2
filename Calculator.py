# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 00:16:21 2020

@author: karis
"""

from tkinter import *

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
                

root = Tk()
cal = Calculator(root)
cal.pack()
root.mainloop()
                
        
        
        