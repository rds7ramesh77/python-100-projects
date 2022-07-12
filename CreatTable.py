#Python program to create Table

#The tabulate module in Python allows us to create and display data in a tabular format which make the data look more readble.

"""""
The tabulate module support these python's data structures
Lists
NumPy Array 
Dictionary 
Pandas DataFrame
"""


from tabulate import tabulate
myData=[["Name","Age","Address","Gender"],["Jhon",25,"KTM","Male"],["Ram",32,"BTW","Male"],["Sita",21,"CTW","Female"]]
print(tabulate(myData))