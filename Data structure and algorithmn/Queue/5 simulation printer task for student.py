'''
Reloaded modules: data_structure_package
Avg wait :  152.27272727272728
Task remaining:  0
Avg wait :  158.41666666666666
Task remaining:  3
Avg wait :  87.16666666666667
Task remaining:  0
Avg wait :  95.6875
Task remaining:  0
Avg wait :  148.96
Task remaining:  0
Avg wait :  30.95
Task remaining:  1
Avg wait :  14.461538461538462
Task remaining:  0
Avg wait :  103.4
Task remaining:  0
Avg wait :  254.6086956521739
Task remaining:  4
Avg wait :  111.0
Task remaining:  1
'''

'''
Class Printer:
    will need to track it's current task and compute the time 
tick :
    decrement the internal timer and sets the printer idle
    

'''
class Printer:
    def __init__(self,ppm):
        self.pagerate=ppm
        self.currentTask=None
        self.timeRemaining=0
    
    def tick(self):
        if self.currentTask !=None:
            self.timeRemaining=self.timeRemaining-1
            if self.timeRemaining<=0:
                self.currentTask=None
    
    def busy(self):
        if self.currentTask !=None:
            return True
        else:
            return False
    
    def startNext(self,newTask):
        self.currentTask=newTask
        self.timeRemaining=newTask.getPages() * 60/self.pagerate

'''
Page number : 1-20 , randomly a page choice 
waitTime: used to retrive the amount time spend in the queue before printing begin

    
'''
import random

class Task:
    def __init__(self,time):
        self.timestamp=time
        self.pages=random.randrange(1,21)
    def getStamp(self):
        return self.timestamp
    def getPages(self):
        return self.pages
    def waitTime(self,currenttime):
        return currenttime-self.timestamp
'''
printQueue: Queue
newPrintTask: decides a new printing task is crated or not
a task can arrive 1-180 seconds

'''
from data_structure_package import Queue
def simulation(numSecnonds,pagesPerMinute):
    labprinter=Printer(pagesPerMinute)
    printQueue=Queue()
    waitingtimes=[]
    
    for currentSencond in range(numSecnonds):
        if newPrintTask():
            task=Task(currentSencond)
            printQueue.enqueue(task)
        if (not labprinter.busy() and (not printQueue.isEmpty())):
            nexttask=printQueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSencond))
            labprinter.startNext(nexttask)
        labprinter.tick()
    avgwait=sum(waitingtimes)/len(waitingtimes)
    #print("Avg wait %6.2f sec %3d task remaining.", %(avgwait,printQueue.size()))
    print("Avg wait : ",avgwait)
    print("Task remaining: ",printQueue.size())
def newPrintTask():
    num=random.randrange(1,181)
    if num==180:
        return True
    else:
        return False
for i in range(10):
    simulation(3600,5)
    