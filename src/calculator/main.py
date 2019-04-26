#!/usr/bin/env python3

from tkinter import *
import calc_lib as calc

calculator = Tk()
calculator.title("Calculator")
calculator.resizable(0, 0)

class Application(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.createWidgets()
        self.a = 0
        self.b = 0
        self.operation = ""
        self.oldA = 0

    def replaceText(self, text):
        newText = str(text)
        if("." in newText):
            newText = newText.rstrip("0").rstrip(".")
        self.display.delete(0, END)
        self.display.insert(0, newText)

    def calculateExpression(self):

        if(self.operation != ""):
            try:
                if(self.operation == "+"):
                    self.result = calc.Addition(self.b,self.a)
                elif(self.operation == "-"):
                    self.result = calc.Subtraction(self.b,self.a)
                elif(self.operation == "*"):
                    self.result = calc.Multiplication(self.b,self.a)
                elif(self.operation == "/"):
                    self.result = calc.Division(self.b,self.a)
                elif(self.operation == "^"):
                    self.result = calc.Exponentiation(self.b,self.a)
                self.replaceText(self.result)
                self.a = ""
                self.b = self.result
                #self.oldA = self.result
                self.operation = ""
            except:
                self.replaceText("ERROR")

    def appendToDisplay(self, text):
        self.entryText = self.display.get()
        self.textLength = len(self.entryText)

        if self.entryText == "ERROR" or self.a == "":
            self.replaceText(text)
        else:
            self.display.insert(self.textLength, text)

        self.a = float(self.display.get())

    def setOperation(self, text):
        if(self.a == "ERROR"):
            return
        if(self.operation == ""):
            if self.b == 0:
                self.operation = text
                self.b = self.a
                self.a = ""
            else:
                if self.a != "" and self.b != 0:
                    self.operation = text
                    self.b = self.a
                    self.a = ""
                else:
                    self.operation = text
                    self.a = ""
        else:
            if self.b == 0:
                self.operation = text
                self.b = self.a
                self.a = ""
            else:
                self.calculateExpression()
                self.operation = text
        

    def calculateA(self, text):
        if(self.b == 0):
            self.b = self.a
            self.a = ""
        if(self.operation != ""):
            self.calculateExpression()
        if(self.b != 0):
            try:
                if text == "!":
                    self.result = calc.Factorial(self.b)
                if text == "√":
                    self.result = calc.Root(self.b,2)
                if text == "ln":
                    self.result = calc.Ln(self.b)
                
                
                self.b = float(self.result)
                self.replaceText(self.b)
            except:
                self.replaceText("ERROR")
                

    def clearText(self):
        self.replaceText("")
        self.a = ""
        self.b = 0
        self.operation = ""
        self.oldA = 0

    def createWidgets(self):
        self.display = Entry(self, font=("Helvetica", 16), borderwidth=1, relief=RAISED, justify=RIGHT)
        #self.display.insert(0, "0")
        self.display.grid(row=0, column=0, columnspan=5, ipady=10)

        self.sevenButton = Button(self, font=("Helvetica", 11), text="7", borderwidth=1, command=lambda: self.appendToDisplay("7"))
        self.sevenButton.grid(row=1, column=0, sticky="NWNESWSE", ipady=10)

        self.eightButton = Button(self, font=("Helvetica", 11), text="8", borderwidth=1, command=lambda: self.appendToDisplay("8"))
        self.eightButton.grid(row=1, column=1, sticky="NWNESWSE", ipady=10)

        self.nineButton = Button(self, font=("Helvetica", 11), text="9", borderwidth=1, command=lambda: self.appendToDisplay("9"))
        self.nineButton.grid(row=1, column=2, sticky="NWNESWSE", ipady=10)

        self.timesButton = Button(self, font=("Helvetica", 11), text="*", borderwidth=1, command=lambda: self.setOperation("*"))
        self.timesButton.grid(row=1, column=3, sticky="NWNESWSE", ipady=10)

        self.clearButton = Button(self, font=("Helvetica", 11), text="C", borderwidth=1, command=lambda: self.clearText())
        self.clearButton.grid(row=1, column=4, sticky="NWNESWSE", ipady=10)
        

        self.fourButton = Button(self, font=("Helvetica", 11), text="4", borderwidth=1, command=lambda: self.appendToDisplay("4"))
        self.fourButton.grid(row=2, column=0, sticky="NWNESWSE", ipady=10)

        self.fiveButton = Button(self, font=("Helvetica", 11), text="5", borderwidth=1, command=lambda: self.appendToDisplay("5"))
        self.fiveButton.grid(row=2, column=1, sticky="NWNESWSE", ipady=10)

        self.sixButton = Button(self, font=("Helvetica", 11), text="6", borderwidth=1, command=lambda: self.appendToDisplay("6"))
        self.sixButton.grid(row=2, column=2, sticky="NWNESWSE", ipady=10)

        self.divideButton = Button(self, font=("Helvetica", 11), text="/", borderwidth=1, command=lambda: self.setOperation("/"))
        self.divideButton.grid(row=2, column=3, sticky="NWNESWSE", ipady=10)

        self.percentageButton = Button(self, font=("Helvetica", 11), text="^", borderwidth=1, command=lambda: self.setOperation("^"))
        self.percentageButton.grid(row=2, column=4, sticky="NWNESWSE", ipady=10)
        

        self.oneButton = Button(self, font=("Helvetica", 11), text="1", borderwidth=1, command=lambda: self.appendToDisplay("1"))
        self.oneButton.grid(row=3, column=0, sticky="NWNESWSE", ipady=10)

        self.twoButton = Button(self, font=("Helvetica", 11), text="2", borderwidth=1, command=lambda: self.appendToDisplay("2"))
        self.twoButton.grid(row=3, column=1, sticky="NWNESWSE", ipady=10)

        self.threeButton = Button(self, font=("Helvetica", 11), text="3", borderwidth=1, command=lambda: self.appendToDisplay("3"))
        self.threeButton.grid(row=3, column=2, sticky="NWNESWSE", ipady=10)

        self.minusButton = Button(self, font=("Helvetica", 11), text="-", borderwidth=1, command=lambda: self.setOperation("-"))
        self.minusButton.grid(row=3, column=3, sticky="NWNESWSE", ipady=10)

        self.minusButton = Button(self, font=("Helvetica", 11), text="√", borderwidth=1, command=lambda: self.calculateA("√"))
        self.minusButton.grid(row=3, column=4, sticky="NWNESWSE", ipady=10)
      


        self.zeroButton = Button(self, font=("Helvetica", 11), text="0", borderwidth=1, command=lambda: self.appendToDisplay("0"))
        self.zeroButton.grid(row=4, column=0, columnspan=2, sticky="NWNESWSE", ipady=10)

        self.dotButton = Button(self, font=("Helvetica", 11), text=".", borderwidth=1, command=lambda: self.appendToDisplay("."))
        self.dotButton.grid(row=4, column=2, sticky="NWNESWSE", ipady=10)


        self.plusButton = Button(self, font=("Helvetica", 11), text="+", borderwidth=1, command=lambda: self.setOperation("+"))
        self.plusButton.grid(row=4, column=3, sticky="NWNESWSE", ipady=10)

        self.minusButton = Button(self, font=("Helvetica", 11), text="!", borderwidth=1, command=lambda: self.calculateA("!"))
        self.minusButton.grid(row=4, column=4, sticky="NWNESWSE", ipady=10)



        self.equalsButton = Button(self, font=("Helvetica", 11), text="=", borderwidth=1, command=lambda: self.calculateExpression())
        self.equalsButton.grid(row=5, column=0,columnspan=4 ,sticky="NWNESWSE", ipady=10)

        self.minusButton = Button(self, font=("Helvetica", 11), text="ln", borderwidth=1, command=lambda: self.calculateA("ln"))
        self.minusButton.grid(row=5, column=4, sticky="NWNESWSE", ipady=10)



app = Application(calculator).grid()
calculator.mainloop()