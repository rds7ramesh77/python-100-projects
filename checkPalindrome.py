#Python program to check Palindrome words

""" panlindrome words are those words that are read the same way frome left to right and right to left."""





def palindrome(sentence):
    for i in (",.'?/><}{{}}'"):
        sentence=sentence.replace(i,"")
    
    palindrome=[]
    
    words=sentence.split('')
    for word in words:
        word=word.lower()
        
        if word==word[::-1]:
            palindrome.append(word)
    return palindrome


sentence=input("Enter a sentence: ")
print(palindrome(sentence))