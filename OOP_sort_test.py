class Person:
	'This is a class defined as Person'
	
	def __init__(self,id=0,name=None,age=0,grade=None):
		#Set the attributes and their default values
		self.id = id
		self.name = name 
		self.age = age
		self.grade = grade
		
	def __repr__(self):
		return 'ID: %d\nName: %s\nAge: %d\nGrade: %s\n' %(self.id,self.name,self.age,self.grade)
		
		
persObj = Person()

datalist = []

persObj.id = 2
persObj.name = 'Amanda'
persObj.age = 33
persObj.grade = 'A' 

datalist.append(persObj)

person2 = Person()
person2.id=4
person2.name='Walter'
person2.age=33
person2.grade = 'B'

datalist.append(person2)


person3 = Person()
person3.id=1
person3.name='Bran'
person3.age=12
person3.grade = 'F'

datalist.append(person3)

person4 = Person()
person4.id=3
person4.name='Cunt'
person4.age=124
person4.grade = 'C'

datalist.append(person4)

print(datalist)

datalist.sort(key = lambda x: x.id,reverse=False)

print(datalist)




