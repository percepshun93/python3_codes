def varArg(*var):
	print(var)
	
def varArg(data,*var):
	print(data,var)
	
def addnum(*var):
	print(var)
	
	sum = 0
	for x in var:
		sum=sum+x
	print (sum)
	
def printData(**var):
	return(var)
	
def printData2(data,**var):
	print(data,var)

def displayDat(name: None, age:None, addr:None):
	print("Name: ", name)
	print('Age: ', age)
	print('Address:', addr)
	
def displayArea(r, pi=3.14):
	return(pi*r*r)