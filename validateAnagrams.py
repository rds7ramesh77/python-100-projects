#Python program for Validate Anagrams
#Validation of anagram words is one of the favourite questions in interviews




def pyAnagram(MyWord1,MyWord2):
    MyWord1=MyWord1.lower()
    MyWord2=MyWord2.lower()
    
    return sorted(MyWord1)==sorted(MyWord2)


print(pyAnagram("men","women"))
print(pyAnagram("logo","olog"))
print(pyAnagram("python","yPhtno"))
print(pyAnagram("hello","hi"))
print(pyAnagram("Nepal","PaleN"))
