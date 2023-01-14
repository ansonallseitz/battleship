#new battleship game. 
#this is a battleship game that has 1 10x10 set of labels 
from tkinter import *


class gameBoard(): 

    def __init__(self): 
        #create tk window
        window=Tk()
        window.title("Lets play battleship")
        window.geometry("1000x700")
        window.columnconfigure((1,2,3,4,5,6,7,8,9,10), weigh=1)
        window.rowconfigure((1,2,3,4,5,6,7), weight=1)
       # for y in range (10):
            #forx in range(10):


        window.mainloop()
gameBoard()

