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
        window.rowconfigure((1,2,3,4,5,6,7,8,9,10), weight=1)

        #create a 10x10 list for the labels 
        lableList = [[0 for colums in range(10)]for rows in range(10)]

        BattleFrame=Frame(window, highlightbackground='blue', highlightthickness="2")
        BattleFrame.grid(row =4, column=5)
        Enterx = Entry(window).grid(row=3, column=9)
        Labelx = Label(window, text=" Please enter the x").grid(row=3, column=8)
        Entery = Entry(window).grid(row=4, column=9)
        Labely = Label(window, text=" Please enter the y").grid(row=4, column=8)
        fireButton = Button(window, text="fire").grid(row=6, column=8)

        #logic to build the matrix of lables 10x10
        y=0
        
        for a in range(10):
            x=0
            for b in range(10):
                lableList[b]=Label(BattleFrame, text=f" {x}_{y} ", borderwidth=1, relief='solid')
                lableList[b].grid(row=a, column=b)
                x+=1
            y+=1
            
        
      




        window.mainloop()
gameBoard()

