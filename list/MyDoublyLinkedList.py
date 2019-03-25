from .MyList import *

class DoublyNode:
    def __init__(self,value,prev,next):
        self.value=value
        self.prev=prev
        self.next=next
        
class DoublyLinkedList(MyList):
    def __init__(self,length):
        self.length=length
        if length == 0:
            self.head=None
        else:
            self.head=DoublyNode(None,None,None)
            node=self.head
            for i in range(length):     
                node.next=DoublyNode(None,None,None)
                node.next.prev=node
                node=node.next                
    
    def __str__(self):
        str='['
        for i in range(self.length-1):
            str += '%s, ' % (self.getNode(i).value)
        return str+'%s]' % (self.getNode(self.length-1).value)    
                
    def getLen(self):
        return self.length
    
    def getNode(self,index):
        newNode=self.head
        for i in range(index):
            newNode=newNode.next
        return newNode
        
    def setValue(self,index,value):
        self.getNode(index).value=value
        return self
    
    def getValue(self,index):
        return self.getNode(index).value
    
    def removeIndex(self,index):
        if self.length==1:
            self.head=None
        elif index==0:
            self.head=self.head.next
            self.head.prev=None
        elif index==self.length-1:
            self.getNode(index-1).next=None
            self.getNode(index).prev=None  ##????
        else:
            self.getNode(index-1).next=self.getNode(index+1)
            self.getNode(index+1).prev=self.getNode(index-1)
        self.length -=1
        return self  
        
    def appendValue(self,value):
        newNode=DoublyNode(value,None,None)
        if self.length==0:
            self.head=newNode
        else:
            self.getNode(self.length-1).next=newNode
            newNode.prev=self.getNode(self.length-1)
        self.length +=1
        return self  
        
    def insertValue(self,index,value):
        newNode=DoublyNode(value,None,None)
        if index==0:
            newNode.next=self.head
            self.head.prev=newNode
            self.head=newNode
        elif index==self.length:
            self.appendValue(value)
        else:
            newNode.next=self.getNode(index)
            self.getNode(index-1).next=newNode
            self.getNode(index).prev=newNode
            newNode.prev=self.getNode(index-1)
        self.length += 1
        return self
    
    def clear(self):
        self.head=None
        self.length=0        