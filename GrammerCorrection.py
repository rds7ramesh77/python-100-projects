#python program for GrammerCorrection 

""" Using correct grammmer is very important in any language. The role  that syntax plays in a programmming lanaguage is what grammer plays in any language."""


""" There are so many application that help you to correct your grammatical mistakes while writing. grammarly is one the best example of such applications."""



""" For this we use Gingerit library """

from gingerit.gingerit import GingerIt


text=input("Enter a sentence:  ")

corrected_text=GingerIt().parse(text)
print(corrected_text)