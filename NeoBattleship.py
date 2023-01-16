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
        
        #set up the frame, the entries and the button
        BattleFrame=Frame(window, highlightbackground='blue', highlightthickness="2")
        BattleFrame.grid(row =4, column=5)
        self.Xentry=StringVar()
        Enterx = Entry(window).grid(row=3, column=9)
        Labelx = Label(window, text=" Please enter the x").grid(row=3, column=8)
        self.Yentry=StringVar()
        Entery = Entry(window, textvariable=self.Xentry).grid(row=4, column=9)
        Labely = Label(window, text="Please enter the y").grid(row=4, column=8)
        self.testVar=StringVar()
        TestEntry = Entry(window, textvariable=self.testVar).grid(row=1, column=1)
        Firebutton = Button(window, text="fire", command=self.processFire).grid(row=5, column=10)

        #define placeholder variables
        e = 'empty'
        s = 'ship'
        #define ship placement. 

        self.shipPlacementlist = [[e, e, e, e, e, e, e, e, e, e],
                                 [e, s, s, s, e, e, e, s, e, e],
                                 [e, e, e, e, e, s, e, s, e, e],
                                 [e, s, e, e, e, s, e, s, e, e],
                                 [e, e, e, e, e, e, e, s, e, e],
                                 [e, e, e, e, e, s, e, s, e, e],
                                 [e, e, e, e, e, e, e, e, e, e],
                                 [e, e, e, s, s, s, s, e, e, e],
                                 [e, e, e, e, e, e, e, e, e, e],
                                 [s, s, e, e, e, e, e, e, e, e]]

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

    def processFire(self):
        xValue = self.formatX(self.Xentry.get())
        if xValue is None:
            self.testVar.set('Bad x value')
            return
        yValue =self.formatY(self.Yentry.get())
        if yValue is None:
            self.testVar.set('Bad y value')
            return


        xValue=int()
        yValue=int()
        #self.testVar.set(self.formatX(xValue))
        #self.testVar.set(self.formatY(xValue))
        firedCoord = self.shipPlacementlist[xValue][yValue]



        self.testVar.set(xValue)


    #validate the input    
    def formatX(self, x):
      if x.isdigit():
        x=int(x)
        if 1 <= x <= 10: 
            return x-1

    #eventually this will be modified to validate A - J
    def formatY(self, y):
      if y.isdigit():
        y=int(y)
        if 1 <= y <= 10: 
            return y-1
                    


gameBoard()

