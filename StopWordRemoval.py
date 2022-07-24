#python program for stop word removal 

""" Stop words removal is an important step while working on any application of natural language processig."""


"""" While working on natural language processing tasks where the o/p dependss on the text we have trained the model on."""

""" tHE NLTK module is used for this """

import nltk 
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')
nltk.download('punkt')



text="Hi there my name is Ramesh Sapkota, i am here to guide you to your journey in Machine Learing  for free."

tokens=word_tokenize(text)

tokenization=[word for word in tokens if not word in stopwords.words('engish')]
print(tokens)
print(tokenization)