#new battleship game. 
#this is a battleship game that has 1 10x10 set of labels 
from tkinter import *


class gameBoard(): 

    def __init__(self): 
        #create tk window, set up the board 
        window=Tk()
        window.title("Lets play battleship")
        window.geometry("1000x700")
        window.columnconfigure((1,2,3,4,5,6,7,8,9,10), weigh=1)
        window.rowconfigure((1,2,3,4,5,6,7), weight=1)

        #create a 10x10 list for the labels 
        lableList = [[0 for colums in range(10)]for rows in range(10)]

        x=0
        y=0
        
        for a in range(10):
            for b in range(10):
                lableList[b]=Label(window, text=f"label {b}")
                lableList[b].grid(row=x, column=y)
                x+=1
                y+=1




        window.mainloop()
gameBoard()

