#Python Program for Queue

#Queues are data structures in computer science that look like lists in Python 

""" Function provie by queue are:
enqueue: it is used to insert a new item into the Queue
dequeue: it is used to remove an item from a queue
is_empty: it returns True if the queue is empty and returns false if the queue is not empty
size: as the name suggests, it returns the number of items in a queue
"""



class Queue:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0, item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)