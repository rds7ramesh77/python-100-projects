#Python program for unicode character removal

""" Unicode character can be defined as the smallest component of any language that has a semantic value."""

""" In computer science,unicode characters are special characters that are not part of any language.



There are 143,859 unicode characters which are divided into the categories mentioned below:
1.Alphanumeric
2.Enclosed Variants 
3.Arrows
4.Mathematical
5.Technical 
6.Musical 
7.Games
8.Emotions
9.And Miscellaneous





The unicode characters contain the alphabets of almost all the known languages. the unicode standard encodes the characters in the range u+0000 and u+10FFF.


For example, the Unicode standard of the happy emoji “😃” that we use while chatting is “U+1F603”.
"""



a="Happy Dashain 😎 May this festival of hindus brings you happpiness,love and joy.😍 Stay safe everyone smilling face with smilling eyes"
a=a.encode('ascii','ignore').decode()
print(a)