# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 21:36:13 2020

@author: Faisal

a
a
b
b
d
Hello
"""
class  BinaryTree:
    def __init__(self,rootObj):
        self.key=rootObj
        self.leftChild=None
        self.rightChild=None
    
    def insertLeft(self,newNode):
        if self.leftChild==None:
            self.leftChild=BinaryTree(newNode)
        else:
            t=BinaryTree(newNode)
            t.leftChild=self.leftChild
            self.leftChild=t
    
    def insertRight(self,newNode):
        if self.rightChild==None:
            self.rightChild=BinaryTree(newNode)
        else:
            t=BinaryTree(newNode)
            t.rightChild=self.rightChild
            self.rightChild=t
    
    def getRightChild(self):
        return self.rightChild
    def getLeftChild(self):
        return self.leftChild
    def getRootValue(self):
        return self.key
    def setRootValue9(self,obj):
         self.key=obj

r=BinaryTree('a')
print(r.key)
print(r.getRootValue())
r.insertLeft('b')
print(r.getLeftChild().key)
r.insertLeft('c')
print(r.getLeftChild().getLeftChild().key)
r.insertRight('d')
print(r.getRightChild().getRootValue())
r.getRightChild().setRootValue9('Hello')
print(r.getRightChild().getRootValue())