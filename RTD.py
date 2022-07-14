#python program for Romam to DECIMALS 

from tkinter.font import ROMAN


tallies={

'I':1,
'V':5,
'X':10,
'L':50,
'C':100,
'D':500,
'M':1000,
#specify more numerals if you wanna
}


def RTD(RomanNmum):
    sum=0
    for i in range(len(RomanNmum)-1):
         left=RomanNmum[i]
         right=RomanNmum[i+1]
    
         if tallies[left]<tallies[right]:
          sum-=tallies[left]
         else:
             sum+=tallies[left]
    sum+=tallies[RomanNmum[-1]]

    return sum    
