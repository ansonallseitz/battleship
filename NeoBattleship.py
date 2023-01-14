#new battleship game. 
#this is a battleship game that has 1 10x10 set of labels 
from tkinter import *


class gameBoard(): 

    def __init__(self): 
        #create tk window
        window=Tk()
        window.title("Lets play battleship")
        window.geometry("1000x700")


        window.mainloop()

