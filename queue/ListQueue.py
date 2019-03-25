from .MyQueue import *


class ListQueue(MyQueue):
    
    def __init__(self):
        self.queue=[]
        print ('---- this is list queue ---')
        
    def put(self,value):
        self.queue.append(value)
    
    def take(self):
        if len(self.queue)==0:
            return None
        else:
            takeValue=self.queue[0]
            self.queue=self.queue[1:]
            return takeValue
        
    def size(self):
        return len(self.queue)
        
    def clear(self):
        self.queue=[]
        
        

