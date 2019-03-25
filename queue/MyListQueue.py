from .MyQueue import *
from list.MyList import *

class MyListQueue(MyQueue):
    
    def __init__(self,myList):
        self.queue=myList
        print ('---- this is Mylist(array list,linked list) queue ---')
    
    def put(self,value):
        self.queue.appendValue(value)
        
    def take(self):
        if self.queue.getLen()==0:
            return None
        else :
            takeValue=self.queue.getValue(0)
            self.queue.removeIndex(0)
            return takeValue
    
    def size(self):
        return self.queue.getLen()
    
    def clear(self):
        self.queue.clear()
        