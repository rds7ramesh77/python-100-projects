#Python program for Recursive Binary Search 
""" 
 Binary Search means to find an item in a sorted array by repeatedly dividing the search interval into two halves and recursive binary seach means to subdivide the entire binary seach process into smaller problems.
    
   """
   




def Recursive_Binary_Search (target,squence,first,last):
       if first>last:
           return False
       else:
           mid=(last+first)//2
           if squence[mid]==target:
               return True
           elif target < squence[mid]:
               return Recursive_Binary_Search(target,squence,first,mid-1)
           else:
               return Recursive_Binary_Search(target,squence,mid+1,last)

               
           