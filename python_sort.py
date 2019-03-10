

from python_class import *
import random as rd
 

def initLinkedList(length):
	l = LinkedList(length)
	for i in range(length):
		l.set(i,rd.randint(0,length))
	return l
	
linkedList=initLinkedList(10)

print (linkedList,linkedList.length)

def insertSort1(linkedList):
	for i in range(1,linkedList.length):
		for j in range(i):
			if linkedList.get(i)<linkedList.get(j):
				linkedList.insertDeleteNode(j,i)
				#linkedList.insertNode(j,linkedList.get(i))
				#linkedList.deleteNode(i+1)
	return linkedList
	




def insertSort3_1(linkedList, value):
	for i in range(linkedList.length):
		if value<linkedList.get(i):	 
			linkedList.insertNode(i,value)
			return linkedList
	linkedList.appendNode(value)
	return linkedList	

def insertSort3_2(linkedList):	
	linkedList2 = LinkedList(0)
	while linkedList.length > 0:
		value = linkedList.get(0)
		linkedList.deleteNode(0)
		insertSort3_1(linkedList2, value)

	linkedList.head = linkedList2.head
	linkedList.length = linkedList2.length
	return linkedList

'''	
def insertSort3_1(linkedList, newNode):
	for i in range(linkedList.length):
		if newNode.value<linkedList.get(i):	 
			linkedList.insertNode(i,newNode.value)
			return linkedList
	linkedList.appendNode(newNode.value)
	return linkedList	

def insertSort3_2(linkedList):	
	linkedList2 = LinkedList(0)
	while linkedList.length > 0:
		value = linkedList.get(0)
		linkedList.deleteNode(0)
		insertSort3_1(linkedList2, Node(value, None))

	linkedList.head = linkedList2.head
	linkedList.length = linkedList2.length
	return linkedList
'''	
	
def insertSort4_1(linkedList):	
	if linkedList.length<=1:
		return linkedList
	else :
		newvalue=linkedList.get(linkedList.length-1)
		linkedList.deleteNode(linkedList.length - 1)
		insertSort4_1(linkedList)
		## todo: insert newNode to linkedList
		
		for i in range(linkedList.length):
			if newvalue<linkedList.get(i):	 
				linkedList.insertNode(i,newvalue)
				return linkedList
		linkedList.appendNode(newvalue)
		
		return linkedList



	
sort_list=insertSort1(linkedList)

print (sort_list)

print (sort_list.head)

#print Node(4,None).value

#print insertSort3_1(sort_list, Node(4,None))
