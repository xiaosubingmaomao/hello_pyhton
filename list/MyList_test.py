from MyArrayList import *
from MyLinkedList import *

def MyArrayList_test():
    l = MyArrayList(10)
    print ('-------array list-------')
    print ('length :',l.getLen())
    
    l.setValue(5,'five')
    print ('index 5 set \'five\' :',l.data)
    
    print ('index 5 value :',l.getValue(5))
    
    print ('remove 5 index',l.removeIndex(5))
    
    print ('append \'hello,append\'',l.appendValue('hello,append'))
    
    print ('on index 0 insert 100',l.insertValue(0,100))
    
    print ('on index 1 insert 10',l.insertValue(10,10))
    
def MyLinkedList_test():
    
    l = MyLinkedList(10)
    print ('-------linked list-------')
    
    print ('length :',l.getLen())
    
    l.setValue(5,'five')
    print ('index 5 set \'five\' :',l)
    
    print ('index 5 value :',l.getValue(5))
    
    print ('remove 5 index',l.removeIndex(5))
    
    print ('append \'hello,append\'',l.appendValue('hello,append'))
    
    print ('on index 0 insert 100',l.insertValue(0,100))
    
    print ('on index 1 insert 10',l.insertValue(10,10))

MyLinkedList_test()