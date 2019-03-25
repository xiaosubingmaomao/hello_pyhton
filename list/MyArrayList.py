print (__name__)
from .MyList import *

class MyArrayList(MyList):  ## inherit

    def __init__(self, length):
        self.data = [None] * length
    
    def __str__(self):
        return 'value:{%s}' % (self.data)
 
    def getLen(self):
        return len(self.data)

    def setValue(self,index,value):
        self.data[index]=value
        return self.data  # return self
    
    def getValue(self,index):
        return self.data[index]  
    
    def removeIndex(self,index):
        self.data=self.data[0:index]+self.data[index+1:len(self.data)]
        return self.data
    
    def appendValue(self,value):
        self.data.append(value)
        return self.data
    
    def insertValue(self,index,value):
        sub_self=self.data[0:index]
        sub_self.append(value)
        newlist=sub_self+self.data[index:len(self.data)]     
        return newlist
    
    def clear(self):
        self.data=[]
        
        


           