class Person:
	'This is a class defined as Person'
	
	def __init__(self,id=0,name=None,age=0,grade=None):
		#Set the attributes and their default values
		self.id = id
		self.name = name 
		self.age = age
		self.grade = grade
		
	def __repr__(self):
		return 'ID: %d\nName: %s\nAge: %d\nGrade: %s' %(self.id,self.name,self.age,self.grade)

	# def deleteRecord(self,id):
		# count = 0
		
		
		
datalist=[]	
while True:
		
		personObj = Person() #define the object which uses specified class
		
		opt=int(input("""
					1. Add Record
					2. Display Record
					3. Delete Record
					4. Sort
					5. Search Record 
					6. Exit\n Enter your Option: """))
		
		if opt == 1:
			#assigning attribute values
			personObj.id = int(input('Enter ID of student: ')) 
			personObj.name = input('Enter Name of student: ')
			personObj.age = int(input('Enter age of student: '))
			personObj.grade = input('Enter the grade of the student: ')
			
			#adding the person object to the list
			datalist.append(personObj)
			
		elif opt == 2:
			#Here x becomes the iterable element in the list. Since the datalist contains every element to be an object (person), x becomes an object as well.
			for xObj in datalist:
				print('________________________')
				print(xObj)
				
		elif opt == 3:
			id = int(input('Enter the id to be deleted: '))
			count = 0
			for xObj in datalist:
					if xObj.id == id:
						del datalist[count]
					count += 1
				
		elif opt == 4:
			#sorting can be done using the key function based on which the list elements will be sorted.
			#key here is taken as the lambda function for x, where x is the attribute 'id' for every object. 
			datalist.sort(key = lambda x : x.id, reverse = False)
			
			for x in datalist:
				print('________________________')
				print(x)
				
		elif opt == 5:
			id = int(input('Enter ID to be searched: '))
			count = 0
			for x in datalist:
				if x.id == id:
					print (datalist[count])
				count += 1
		
		else:
			break
				
			
