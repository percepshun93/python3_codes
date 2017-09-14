#Question 4

# n = int(input('Enter the number of values you want to see: '))

# list1 = []
# for i in range(n):
	# i = int(input('Enter a number: '))
	# list1.append(i)
	# tp = tuple(list1)
	
# print(list1)	
# print (tp)
#----------------------------------------------------------------------------------

#Question 5

# class Test:
	# 'This is a class defined for testing 2 methods getString and printString'
	
	# def __init__(self):
		# self.what = ''

	# def getString(self):
		# self.what = input('Enter a string: ')
		
	# def printString(self):
	  # print (self.what)

		
# test = Test()
# test.getString()
# test.printString()
#----------------------------------------------------------------------------------

#Question 6

# import math 

# num = int(input('How many items do you want?: '))
# C = 50
# H = 30

# list1 = []

# for i in range (num):
	# D = float(input('Enter a number: '))
	# list1.append(D)

# list2 = []	

# for D in list1:
	# Q = round(math.sqrt((2*C*float(D)/H)))
	# list2.append(Q)
	
# print (list1)
# print (list2)
#-------------------------------------------------------------------------------
	
#Question 7

#look into it
#-------------------------------------------------------------------------------

#Question 8 

# num = int(input('Enter the number of words: '))

# list_words = []

# for i in range(num):
	# word = input('Enter a word: ')
	# list_words.append(word)
	# list_words.sort()
	
# print('Sorted list is: ',list_words)
#-------------------------------------------------------------------------------


# Prime number generator

def isPrime(num):
		if num == 0 or num == 1:
			return False
			
		elif num == 2:
			return True
			
		for x in range(2,num):
			if num % x == 0:
				return False
				
		else:
			return True
			
n = int(input('Enter the number of primes you want: '))

i = 0
numlist = []
numlist.append(i)
primes_list = []

while len(primes_list) < n:
	i = i+1
	numlist.append(i)
	primes_list = list(filter(isPrime,numlist))
		
print ('The first %d primes are: ' %(len(primes_list)), primes_list)
print(len(numlist))
#-------------------------------------------------------------------------------------