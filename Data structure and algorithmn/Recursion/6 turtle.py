# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 12:25:47 2020

@author: Faisal
"""
import turtle
myTurtle=turtle.Turtle()
myWin=turtle.Screen()
def drawSpiral(myTurtle,lineLen):
    if lineLen>0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        drawSpiral(myTurtle,lineLen-5)
drawSpiral(myTurtle,100)
myWin.exitonclick()