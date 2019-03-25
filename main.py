
from queue.ListQueue import *
from queue.MyListQueue import *
from queue.MyQueueTest import *
from list.MyLinkedList import *
from list.MyArrayList import *

a=MyQueueTest(MyListQueue(MyArrayList(0)))

a.allTest()


print ('*********************************')
b=MyQueueTest(ListQueue())

b.allTest()


print ('*********************************')
a=ListQueue()
a.put('a')

a.put('ab')

a.put('abc')

print(a.size())