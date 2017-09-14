from sys import *

class USB:
	version = 3.0
	
	def __init__(self):
		self.__private_var = 1.33
		self.public_var = 2.33
		
	def read(self):
		print ('This is read method from the superclass USB')
		
	def write(self):
		print ('This is write method from the superclass USB')
		
#defining a subclass to USB requires the superclass USB to be passed as a parameter to the subclass Pendrive
		
class Pendrive(USB):
	def __init__(self, capacity=10,color='black',brand='Transcend', data= ' '):
		super().__init__() #this is done to ensure that the superclass variables/attributes get inherited to the subclass
		self.cap = capacity
		self.clr = color
		self.brand = brand
		self.dat = data

	def read(self):
		#print('This is read method from the subclass Pendrive')
		return 'Content: %s' %(self.dat)
		
	def write(self,content = ' '):
		#print ('This is write method from the subclass Pendrive')
		return 'Content: %s' %(self.dat+' '+content)
		
	def size(self,content = ' '):
		dat_size = getsizeof(pd.write(content))
		rem_size = self.cap - dat_size
		return 'Remaining memory: %d' %(rem_size)
		
pd = Pendrive(color = 'red', data = 'This is a test string')
pd.read()

pd.write('This is a string to be added')
pd.size('This is a string to be added')

