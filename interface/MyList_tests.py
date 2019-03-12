from MyList import MyList
from MyLinkedList import MyLinkedList
from MyArrayList import MyArrayList
from MyDoublyLinkedList import DoublyLinkedList

class MyListTest:
    
    def __init__(self,myList):
        self.list=myList
    
    def getLenTest(self):
        self.list.clear()
        
        print ('length == 0: %s' % self.list.getLen())
        
        self.list.appendValue(1)
        print ('length == 1: %s' % self.list.getLen())
        
        self.list.removeIndex(0)
        print ('length == 0: %s' % self.list.getLen())
    
    def setValueTest(self):
        self.list.clear()
        self.list.appendValue(1)
        print ('value at index %s: %s' % (0, self.list.getValue(0)))
        
        self.list.setValue(0, 2)
        print ('value at index %s == 2: %s' % (0, self.list.getValue(0) == 2))
        
    def getValueTest(self):
        self.list.clear()
        self.list.appendValue(0)
        self.list.appendValue(1)
        self.list.appendValue(2)
        print ('value at index %s: %s' % (0, self.list.getValue(0)))
        print ('value at index %s: %s' % (1, self.list.getValue(1)))
        print ('value at index %s: %s' % (2, self.list.getValue(2)))
    
    def removeIndexTest(self):
        self.list.clear()
        self.list.appendValue(0)
        self.list.appendValue(1)
        
        print ('original list :', self.list)
        
        print ('remove index %s ,the list : %s' % (0 , self.list.removeIndex(0)))
        
    def appendValueTest(self):
        self.list.clear()
        print ('append %s ,the list :%s' % (100,self.list.appendValue(100))) 
    
    def insertValueTest(self):
        self.list.clear()
        self.list.appendValue(0)
        self.list.appendValue(1)
        self.list.appendValue(2)
        print ('original list :', self.list)
        print ('at index %s insert value %s ,the list is %s' %(2,200 ,self.list.insertValue(2,200)))
            
    def TestAll(self):
        self.getLenTest()
        print ('')
        self.setValueTest()
        print ('')
        self.getValueTest()
        print ('')
        self.appendValueTest()
        print ('')
        #self.removeIndexTest()
        print ('')
        self.insertValueTest()
        

test = MyListTest(MyLinkedList(0))
test.TestAll()

print ('-----array list-------')
test = MyListTest(MyArrayList(0))
test.TestAll()
print ('-----doubly list-------')
test = MyListTest(DoublyLinkedList(0))
test.TestAll()