#python program to convert currency

""" To convert one currency to another, we need to write a program to accept user input where the user will enter the amount of money, and the user has to choose the type of currency the user wants to check the value of"""

""" For this Python provide forex library """


from unittest import result
from forex_python.converter import CurrencyRates

CURR=CurrencyRates()

amount=int(input("Enter the amount: "))
fromCurrency=input("From Currency: ").upper()
toCurrency=input("To Currency: ").upper()

print(fromCurrency, "To" , toCurrency,amount)
result=CURR.convert(fromCurrency,toCurrency,amount)

print(result)