#Python program for Hash Table 

""" Hash Tables are like a dictionaries in Python 

A hash table is based on the concept of hashing which provides a way to store and retrieve a data efficently in the complexities of time and space.
And used in :

Database indexing 
Complier Design 
Caching 
Password Authentication 
Error Analysis 
And Many More"""


class MyHashTable:
    def __init__(self, items):
        self.bucket_size = len(items)
        self.buckets = [[] for i in range(self.bucket_size)]
        self.assign_buckets(items)

    def assign_buckets(self, items):
        for key, value in items:
            hash_value = hash(key)
            index = hash_value % self.bucket_size
            self.buckets[index].append((key, value))
            
    def get_value(self, input_keys):
        hash_value = hash(input_keys)
        index = hash_value % self.bucket_size
        bucket = self.buckets[index]
        for key, value in bucket:
            if key == input_keys:
                return(value)