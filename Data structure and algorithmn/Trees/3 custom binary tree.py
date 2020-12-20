# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 22:26:24 2020

@author: Faisal
a
b
d
c
e
"""
class BinaaryTree:
    def __init__(self,obj):
        self.key=obj
        self.leftChild=None
        self.rightChild=None
    def insertLeft(self,newNode):
        if self.leftChild==None:
            self.leftChild=BinaaryTree(newNode)
    
    def insertRight(self,newNode):
        if self.rightChild==None:
            self.rightChild=BinaaryTree(newNode)
        
            
    
tree=BinaaryTree('a')
print(tree.key)
tree.insertLeft('b')
print(tree.leftChild.key)
tree.leftChild.insertRight('d')
print(tree.leftChild.rightChild.key)

tree.insertRight('c')
print(tree.rightChild.key)
tree.rightChild.insertLeft('e')
tree.rightChild.insertRight('f')
print(tree.rightChild.leftChild.key)
