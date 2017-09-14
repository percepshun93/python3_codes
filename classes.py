class Employee:
	empcount = 0
	
	def __init__(self,name=None,age=0,salary=0):
		
		self.name = name
		self.age = age
		self.salary = salary
	
		Employee.empcount += 1
		
	def display(self):
		print('name: %s\nage: %d\nsalary: %0.2f' %(self.name,self.age,self.salary))
		
		
nam = input('Enter name: ')
ag = int(input('Enter Age: '))
sal = float(input('Enter Salary: '))

emp1 = Employee(nam,ag,sal)
emp1.display()