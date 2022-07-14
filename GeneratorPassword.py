#Python program to generate Password

import random 

PasswordLength=int(input("Enter the length of password::"))

source="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

NewPassword="".join(random.sample(source,PasswordLength))

print(NewPassword)