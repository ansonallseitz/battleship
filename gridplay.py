from tkinter import *


#so the first step I'm taking is an attempt at drawling the board out. 
class Battleship: 
    def __init__(self): 
        window =Tk()
        window.title("Lets play battleship")
        window.geometry("1500x900")
        window.columnconfigure((1, 2, 3, 4, 5, 6, 7, 8, 9, 10), weight =1)
        window.rowconfigure((1, 2, 3, 4, 5, 6, 7, 8, 9, 10), weight =1)
       

      #  self.bttn2 =Button(text="placeholder2").grid(row=4)

        self.bttn1 =Button(text="placeholder").grid(row=6)
        #self.bttn1.grid(row=1, column=10)
        
        window.mainloop()
Battleship()