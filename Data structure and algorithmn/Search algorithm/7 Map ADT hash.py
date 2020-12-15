# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 21:38:33 2020

@author: Faisal

Map operation:
    Map() -> new Map
    put(key,val) ->  map pair key,value
    get(key) -> return store value
    del -> delete a map value
    len() -> length of pairs
    in-> True, False
[77, 44, 55, 20, 26, 93, 17, None, None, 31, 54]
['bird', 'goat', 'pig', 'chicken', 'dog', 'lion', 'tiger', None, None, 'cow', 'cat']
"""
class HashTable:
    def __init__(self):
        self.size=11
        self.slots=[None]* self.size
        self.data=[None]*self.size
    
    def hashfunciton(self,key,size):
        return key%size
    
    def put(self,key,data):
        hashvalue=self.hashfunciton(key,len(self.data))
        if self.slots[hashvalue]==None:
            self.slots[hashvalue]=key
            self.data[hashvalue]=data
        else:
            if self.slots[hashvalue]==key:
                self.data[hashvalue]=data
            else:
                nextslot=self.rehash(hashvalue,len(self.slots))
                while self.slots[nextslot] !=None and self.slots[nextslot]!=key:
                    nextslot=self.rehash(nextslot,len(self.slots))
                if self.slots[nextslot]==None:
                    self.slots[nextslot]=key
                    self.data[nextslot]=data
                else:
                    self.data[nextslot]=data
    def rehash(self,oldhash,size):
        return (oldhash+1)%size
    
    def get(self,key):
      startslot = self.hashfunction(key,len(self.slots))
    
      data = None
      stop = False
      found = False
      position = startslot
      while self.slots[position] != None and  \
                           not found and not stop:
         if self.slots[position] == key:
           found = True
           data = self.data[position]
         else:
           position=self.rehash(position,len(self.slots))
           if position == startslot:
               stop = True
      return data
    
    def __getitem__(self,key):
        return self.get(key)
    
    def __setitem__(self,key,data):
        self.put(key,data)
        
            
H=HashTable()
H[54]="cat"
H[26]="dog"
H[93]="lion"
H[17]="tiger"
H[77]="bird"
H[31]="cow"
H[44]="goat"
H[55]="pig"
H[20]="chicken"
print(H.slots)
print(H.data)