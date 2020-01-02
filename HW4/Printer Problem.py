#!/usr/bin/env python
# coding: utf-8

# In[35]:


from pythonds.basic.queue import Queue
import random
class Printer:
    def __init__(self,ppm):
        self.speed=ppm
        self.curtask=None
        self.remtime=0
    
    def tick(self):
        if self.curtask!=None:
            self.remtime-=1
            if self.remtime<=0:
                self.curtask=None

    def busy(self):
        return self.curtask!=None
    
    def startnew(self,newtask):
        self.curtask=newtask
        self.remtime=newtask.getpage()/self.speed*60

class Task:
    def __init__(self,time):
        self.timestamp=time
        self.pages=random.randrange(1,21)
        
    def getstamp(self):
        return self.timestamp
    
    def getpage(self):
        return self.pages
    
    def waittime(self,curtime):
        return curtime-self.timestamp

import random
def newtask():
    rand=random.randrange(1,181)
    if rand == 180:
        return True
    else:
        return False
def simulation(numSeconds,ppm):
    labprinter=Printer(ppm)
    printq=Queue()
    waitingtime=[]
    for i in range(numSeconds):
        if newtask():
            task=Task(i)
            printq.enqueue(task)
        if (not labprinter.busy()) and (not printq.isEmpty()):
            nextprint=printq.dequeue()
            waitingtime.append(nextprint.waittime(i))
            labprinter.startnew(nextprint)
        labprinter.tick()
    averagewaittime=sum(waitingtime)/len(waitingtime)
    print('Average wait time %6.2f secs and %3d tasks remaining.' %(averagewaittime,printq.size()))


# In[36]:


for i in range(20):
    simulation(3600,5)


# In[37]:


for i in range(20):
    simulation(3600,10)

