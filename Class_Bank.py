#import random
#acc = random.randrange(100000,999999)

class Bank:
	'This is a class for variables using type: Bank'
	#acc = random.randrange(100000,999999)
	
	def __init__(self,id=0,name=None,age=0,addr=None):
		self.id = id
		self.name = name
		self.age = age
		self.addr = addr
		
	def __repr__(self):
		return 'Details:\nID: %d\nHolder\'s Name: %s\nAge: %d\nHolder\'s Address: %s' %(self.id,self.name,self.age,self.addr)
		
	def createAcc(self):
		print('Enter your details: ')
		pass
		
	def withdraw(self):
		pass
		
	def deposit(self):
		pass
		
datalist = []

while True:
	bankObj = Bank() #define the object which uses specified class
		
	opt=int(input("""
					Please select an Option\n
					1. Create an account
					2. Withdraw amount
					3. Deposit amount
					4. Display account details
					5. Exit\n
					Enter your Option: """))
		
	if opt == 1:
			#assigning attribute values
			print('Enter your details: ')
			bankObj.id = int(input('Enter ID: ')) 
			bankObj.name = input('Enter Account Holder\'s Name: ')
			bankObj.age = int(input('Enter Account Holder\'s Age: '))
			bankObj.addr = input('Enter Account Holder\'s Address: ')
			
			datalist.append(bankObj)
			
	elif opt == 2:
			pass
				
	elif opt == 3:
			pass
				
	elif opt == 4:
			print (bankObj)
		
	else:
			break