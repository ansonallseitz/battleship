from tkinter import *


#so the first step I'm taking is an attempt at drawling the board out. 
class Battleship: 
    def __init__(self): 
        window =Tk()
        window.title("Lets play battleship")
        window.geometry("1500x900")

        self.player1Board = Canvas( width = 500, height = 500, bg="blue")
        self.player1Board.grid(row = 10, column = 0)
        for y in range (10):
            for x in range (10):
                self.player1Board.create_rectangle(x*50, y*50, (x+1)* 50, (y+1)*50)

        window.mainloop()
Battleship()