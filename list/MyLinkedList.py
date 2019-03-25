
from .MyList import *

class Node:

    def __init__(self, value, next):
        self.value = value
        self.next = next
        
    def __str__(self):
        return 'value:{%s}, next node: {%s}' % (self.value, self.next)
    
class MyLinkedList(MyList):  
    
    def __init__(self,length):  #initialize
        self.length=length
        if self.length==0:
            self.head=None
        else:
            self.head = Node(None, None)        
            node=self.head
            for i in range(self.length-1):
                node.next=Node(None, None)
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
        if index==0:
            self.head=self.head.next
        else :
            self.getNode(index-1).next=self.getNode(index).next
        self.length -= 1
        return self
    
    def appendValue(self,value):
        newnode=Node(value,None)
        if self.length==0:
            self.head=newnode
        else:
            self.getNode(self.length-1).next=newnode
        self.length += 1
        return self
    
    def insertValue(self,index,value):
        newnode=Node(value,None)
        if index==0:
            newnode.next=self.head
            self.head=newnode
        else:
            newnode.next=self.getNode(index)
            self.getNode(index-1).next=newnode
        self.length += 1
        return self
    
    
    def clear(self):
        self.head=None
        self.length=0