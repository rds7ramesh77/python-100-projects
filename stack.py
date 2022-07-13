#Python program for Stack

#The stack is a data structure that looks like a list in Python where you can add and remove items.


class MyStack:
    def __init__(self):
        self.items=[]
    
    def is_empty(self):
        return self.items==[]
    
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        l = len(self.items)-1
        return self.items[l]
    
    def size(self):
        return len(self.items)
    
    
    
    
stack = MyStack()
print(stack.is_empty()) 

for i in range(0, 50):
    stack.push(i)
print(stack.size())
print(stack.items)