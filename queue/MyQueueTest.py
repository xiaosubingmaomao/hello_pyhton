

class MyQueueTest:
    
    def __init__(self,myQueue):
        self.queue=myQueue
        
    def putTest(self):
        print ('  put 1 ')
        self.queue.put(1)
        print ('  put 2 ')
        self.queue.put(2)
        print ('  put 3 ')
        self.queue.put(3)
        print ('  put 4 ')
        self.queue.put(4)
        
    
    def takeTest(self):
        self.queue.clear()
        self.queue.put("a")
        self.queue.put("ab")
        self.queue.put("abc")
        self.queue.put("abcd")
        print (' queue size : ',  self.queue.size())
        print ('  take 1 :',self.queue.take())
        
        print (' queue size : %s' % self.queue.size())
        print ('  take 2 ',self.queue.take())
        
        print (' queue size : %s' % self.queue.size())
        print ('  take 3 ',self.queue.take())
        
        print (' queue size : %s' % self.queue.size())
        print ('  take 4 ',self.queue.take())
        
        print (' queue size : %s' % self.queue.size())
        
    def allTest(self):
        self.putTest()
        self.takeTest()