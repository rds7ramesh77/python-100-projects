#python program for language detection

""" for this we use the module called langdetect package 


Python can detect 55 language in this package"""


from langdetect import detect

text=input("Enter any text in any language:  ")
print(detect(text))


#the o/p received is an abbreviated form of the languege ( en means english hi means hindi)