#Python program to create Chat Bot

""" A chat bot is an AI application that mimics human conversations. It is widely used by companies to slove the most common problems they receive from customers daily.

Here I will be using the NLTK library in python which is one of the best python libraries fro any task of natural language processing:"""


from nltk.chat.util import Chat, reflections

#Nepal is a list of patterns and responses

nepal=[
    [ 
     r"(.*) my name is (.*)",
     [ "Hello %2, How are you today ?",]
     
     
     ],
    
    [ 
     r"(.*) your name?",
     [ "My name is CuteBot,But you can just call me bot and I am a chatbot.",]
     
     
     ],
    
    [ 
     r"(.*)how are you ?",
     ["I'm doing very well","i am great !" ],
     ],
]