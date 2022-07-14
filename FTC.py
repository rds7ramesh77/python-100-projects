#python program to create Fahrenheit To Celsius 

from types import CellType


def FTC(Fahrenheit):
    Fahrenheit=float(input("Enter Temp: "))
    Celsius=5/9*(Fahrenheit-32)
    return Celsius 
print(FTC(78))