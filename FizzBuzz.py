#Python program for Fizz Buzz Algorithm 

""" The FizzBuzz algorithm is one of the favourite questions in coding interviews. 
Fizz and Buzz refer to any number that is multiple fo 3 and 5"""


""" The FizzBuzz algo comes from a children's game. The algo has been one of the fav coding interview ques for a very long time."""


""" n this problem, you are given a range of integers and you need to produce output according to the rules mentioned below:

If the integer (x) is divisible by 3, the output must be replaced by “Fizz”.
If the integer (x) is divisible by 5, the output must be replaced by “Buzz”.
If the integer (x) is divisible by 3 and 5, the output should be replaced by “FizzBuzz”."""



number =int(input("Enter any positive number:"))



for i in range(number ): #or you can provide range as for i in range(1,90)
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)