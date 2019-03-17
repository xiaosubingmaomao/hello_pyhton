
class FatPerson:
	
	
	def __init__(self,name,gender):
		self.name=name
		self.__gender=gender
		self.__print() 
	
	def __print(self):
		print (self.name,' is a new fat', self.__gender,' person!')


		
obj=FatPerson('zxp','male')

print(obj.name)

print(obj.__gender)

