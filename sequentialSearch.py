#Python program for Sequential Search
#The searching algorithms are the algorithms that are used to search a particular value in a data structure such as list.

def sequentialSearch(mylist,n):
    found=False
    
    for i in mylist:
        if i==n:
            found=True
            
            break
    return found

numbers=list(range(1,30))
print(sequentialSearch(numbers,11))