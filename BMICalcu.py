#Python program to create BMI Claculator 


""" 
BMI is a measure of relative weight based on an individual's mass and height"""



Height=float(input("Enter Your Height in CM: "))
Weight=float(input("Enter your Weight in kg:"))

Height=Height/100

BMI=Weight/(Height*Height)

print("Your Body Mass Index (BMI) is: ",BMI)
if(BMI>0):
    if (BMI<=16):
     print("You are severely underweight")

    elif(BMI<=18.5):
     print("You are underweight")
    elif(BMI<=25):
     print("Your are healthy")
    elif(BMI<=30):
     print("You are overweight") 
    else:
     print("you are severely overweight")
       
else:
    print("Invalid Details")