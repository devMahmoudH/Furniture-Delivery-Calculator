#A calculator for delivery 
#Created by Mahmoud
#For Discount Furniture & Linen
#---------------------------------------------------------------------------------

from tkinter import *
from tkinter.messagebox import showinfo
import sys
import os


win = Tk()

win.title("Delivery Calculator") #title of the app

appLogo = PhotoImage(file = "C:/Users/Mahmo/Desktop/Delivery Calculator Beta/elements/appicon.png")
win.iconphoto(False, appLogo) #Icon of the opened app

#Flat Rate Variable
#-----------------------------------------------------------------------------------

flatRate = "$40" #$40 is the flat rate


#Function of the Delivery fee (To Be Completed)
#------------------------------------------------------------------------------------
#def fee():


#Calculation Formula
#------------------------------------------------------------------------------------
def calculation():
    x1 = entry1.get() #Get Miles Entry
    if (int(x1) <= 15):
        showinfo("Delivery Fee", "Delivery Fee is "+ str(flatRate))
    elif (int(x1) >= 30 ):
        showinfo("Delivery Fee", "Delivery Fee is $60")
    #elif (selectFloor) != True:
        #showinfo("Select Floors","Please Select Number of Floors")
    else:
        showinfo("Invalid", "Please Enter a Valid Vlaue!")


#Discount Furniture & Linen Title 
#---------------------------------------------------------------------
logo = PhotoImage(file="C:/Users/Mahmo/Desktop/Delivery Calculator beta/elements/logo_transparent.png")
labelTitle = Label(win,text="Discount Furni+ture & Linen Delivery Calculator", font=("arial",18,"bold"))
labelTitle.config(image=logo)
labelTitle.grid(row=0,column=1)

#Enter Miles Label
#--------------------------------------------------------------------
labelMiles = Label(win,text="Enter Miles: ", font=("arial",10,"bold"))
labelMiles.grid(row=1,column=1,sticky="W")

entry1 = Entry(win,font=("arial",10,"bold"))
entry1.grid(row=1,column=1)

#Function of Floors checkbox to select number of floors
#----------------------------------------------------------------------

def selectFloor():
    chk_state = BooleanVar()
    chk_stateTwo = BooleanVar()
    chk_stateThree = BooleanVar()

    chk_state.set(True) #set check state

    firstFloor = Checkbutton(win, text ="First Floor", var=chk_state)
    firstFloor.grid(row=1,column=1, sticky="E")
    secondFloor = Checkbutton(win, text ="Second Floor", var=chk_stateTwo)
    secondFloor.grid(row=2,column=1, sticky="E")
    thirdFloor = Checkbutton(win, text ="Third Floor", var=chk_stateThree)
    thirdFloor.grid(row=3,column=1, sticky="E")

selectFloor()


#Enter Number floors Drop down Menu (Doing Check box better)
#---------------------------------------------------------------------
#variable = StringVar(win)
#variable.set("Select Floor") #Default Value

#w = OptionMenu(win, variable, "Select Floor","First Floor", "Second Floor", "Third Floor")
#w.grid(row=3,column=1)

#Drop down menu to select package (Sofa loveseat, Mattress, Bedroom set)
#-----------------------------------------------------------------------
#packageVariable = StringVar(win)
#packageVariable.set("Select Package") # Defualt Value

#p = OptionMenu(win, packageVariable, "Select Package", "Basic")


#Output Box (In Progress)
#------------------------------------------------------------------------
labelOutput = Label(win,text="Delivery Fee: ", font=("arial",10,"bold"))
labelOutput.grid(row=4,column=1,sticky="W")
userOutput = Text(win,width = 10, height=1, text=flatRate)
userOutput.grid(row=4,column=1)

#Calculate Delivery Button
#--------------------------------------------------------------------------
img = PhotoImage(file="C:/Users/Mahmo/Desktop/Delivery Calculator beta/elements/button_calculate.png")
buttonCalc = Button(win,text="Calculate Delivery", font=("arial",12,"bold") , command = calculation)
buttonCalc.config(image=img)
buttonCalc.grid(row=5,columnspan=2)


win.mainloop()

