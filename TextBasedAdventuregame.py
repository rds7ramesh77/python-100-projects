#Python program to create text based adventure game

name=str(input("Hello!, Enter Your Name::"))
print(f"{name} You are stuck at work")
print("you are still working and suddendly you saw a ghost, Now you have two opetions...")
print("1.Run.2.jump from window")

user=int(input("Choose 1 or 2 : "))

if user==1:
    print("You did it")
elif user==2:
    print("You are not that smart")
else:
    print("Please CHECK input")