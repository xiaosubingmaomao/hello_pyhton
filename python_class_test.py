from python_class import *

def LinkedLIst_get_test():
	l = LinkedList(10)
	v = l.get(1)
	print True if v == None else False

	l.set(8,'uu')
	print l.get(8)
	
	print l.get(7)

	print l.getNode(3)

	print l


	l.insertNode(3,'ins')

	print l, '\n', l.length

	l.insertNode(0,'ins0')

	print l, '\n', l.length

	l.insertNode(12,'ins_end')

	print l, '\n', l.length

	l.deleteNode(2)

	print l, '\n', l.length
	
	l.deleteNode(0)

	print l, '\n', l.length

	l.deleteNode(10)

	print l, '\n', l.length

	l.appendNode('appd')

	print l, '\n', l.length

	



LinkedLIst_get_test()
