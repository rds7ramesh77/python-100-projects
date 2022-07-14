#   Python program for Dice Simulator 

import random

minimum_Value=1
maximum_value=6


roll_Again="yes"
while roll_Again=="yes" or roll_Again=="y":
    print("Rolling The Dices...")
    print("The Value Are...")
     
     
    print(random.randint(minimum_Value,maximum_value))
    print(random.randint(minimum_Value,maximum_value))
 
    roll_Again=input("Roll the Dice Again???")    
    