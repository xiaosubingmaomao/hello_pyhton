
class Node:

	def __init__(self, value, next):
		self.value = value
		self.next = next
		
	def __str__(self):
		return 'value:{%s}, next node: {%s}' % (self.value, self.next)

class LinkedList:  

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

	def getNode(self,index):
		node=self.head
		for i in range(index):
			node=node.next
		return node
		
	def get(self,index):
		return self.getNode(index).value
	
	def set(self,index,value):
		self.getNode(index).value=value
	
	def insertNode(self,index,value):
		self.length += 1
		if index == 0:
			addnode=Node(value,self.head)
			self.head=addnode
		elif index==self.length:
			appendNode(self,value)
		else:
			addnode=Node(value,self.getNode(index-1).next)   #   addnode=Node(value,self.getNode(index))
			self.getNode(index-1).next=addnode
		
	def deleteNode(self,index):
		self.length -= 1
		if index == 0:
			self.head=self.head.next
		else:
			self.getNode(index-1).next=self.getNode(index).next
		
	def appendNode(self,value):
		newnode=Node(value,None)
		if self.length==0:
			self.head=newnode
		else:
			self.getNode(self.length-1).next=newnode
		self.length += 1
		
	def insertDeleteNode(self,insert_index,delete_index):  ## insert_index < delete_index
		newNode=self.getNode(delete_index)
		self.getNode(delete_index-1).next=newNode.next
		if insert_index==0:		
			newNode.next=self.head
			self.head=newNode
		else: 
			newNode.next=self.getNode(insert_index)
			self.getNode(insert_index-1).next=newNode
			
		
	