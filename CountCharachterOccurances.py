#python program to count character occurrences

#to count the occurrences of a character, we need to write an algorithm that returns the number of time each character appears in the input string.



def characters_count(str):
    count={}
    
    for i in str:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
            
    print(count)
print(characters_count("HelloThereIamFromNepal"))

 
   #Output: 'H': 1, 'e': 4, 'l': 3, 'o': 2, 'T': 1, 'h': 1, 'r': 2, 'I': 1, 'a': 2, 'm': 2, 'F': 1, 'N': 1, 'p': 1
   