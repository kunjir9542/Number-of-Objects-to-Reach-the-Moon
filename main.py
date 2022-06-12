from math import trunc
from random import randint
score = 0
numWrong = 0
multiplier = 1
def titleScreen():
    choice = input("Hello! Do you want to figure out how many of an object of your choosing would it take to reach the moon? (Y/N)")
    if choice == "Y":
        calculateAmount()

def calculateAmount():
    global multiplier

    print("-------------------------------------------------------------------------")
    objName = input("What is the name of your object?")
    print("-------------------------------------------------------------------------")
    unitMeasurement = input("Enter what unit of measurement we should use for your object \n 1) Miles \n 2) Yards \n 3) Feet \n 4) Inches")
    if unitMeasurement == 1:
        multiplier = 1
    elif unitMeasurement == 2:
        multiplier = 1780
    elif unitMeasurement == 3:
        multiplier = 5280
    elif unitMeasurement == 4:
        multiplier = 63360
    print("-------------------------------------------------------------------------")
    measurement = input("What is the length of your object?")
    print("-------------------------------------------------------------------------")

    numOfObjects = 238990 * multiplier / int(measurement)

    print("It would take about " + str(int(numOfObjects)) + " " + objName + " to reach the moon!")








titleScreen()

