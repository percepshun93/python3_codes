import random

class Bank:
	'This is a class for variables using type: Bank'
	
	def __init__(self, id = 0, name = ' ', amt = 0, addr = ' ',acc = 0):
		self.id = id
		self.name = name
		self.amt = amt
		self.addr = addr
		self.acc = acc
		
	def __repr__(self):
		return 'Details:\nID: %d\nName: %s\nAmount: %d\nAddress: %s\nAccount Number: %d' %(self.id,self.name,self.amt,self.addr,self.acc)
		
	def createAcc(self):
		return 'Account has been created'

datalist = []

while True:
	#bankObj = Bank() #define the object which uses specified class
		
	opt=int(input("""
					Please select an Option\n
					1. Create an account
					2. Withdraw amount
					3. Deposit amount
					4. Display account details
					5. Exit\n
					Enter your Option: """))
		
	if opt == 1:
		bankObj = Bank()
		bankObj.id = int(input('Enter ID: ')) 
		bankObj.name = input('Enter Account Holder\'s Name: ')
		bankObj.amt = int(input('Enter Amount: '))
		bankObj.addr = input('Enter Account Holder\'s Address: ')
		bankObj.acc = random.randrange(100000,999999) 
		
		bankObj.createAcc()
		
		datalist.append(bankObj)
			
	elif opt == 2:
			id = int(input('Enter your Account ID: '))
			withdraw_amt = int(input('Enter amount to be withdrawn: '))
			count = 0
			for x in datalist:
				if x.id == id:
					if x.amt < 10000:
						print ('Insufficient Funds. Minimum balance of 10,000 required')
						continue
					else:
						x.amt = x.amt - withdraw_amt
						print ('Current account details:\n',datalist[count])
				count += 1
								
	elif opt == 3:
			id = int(input('Enter your Account ID: '))
			dep_amt = int(input('Enter amount to deposit: '))
			
			count = 0
			for x in datalist:
				if x.id == id:
					x.amt = x.amt + dep_amt
					print ('Current account details:\n',datalist[count])
				count += 1
	
	elif opt == 4:
			for x in datalist:
				print ('_________________________')
				print (x)
		
	else:
			break