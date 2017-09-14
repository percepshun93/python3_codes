#Initialize empty list
dat_list = []
	
def read_data(id,name,age,grade):
		dict1 = {'ID of student':id, 'Name of Student':name, 'Age of student':age,'Grade of student':grade}
		dat_list.append(dict1)
		return dat_list

	
while True:
	a = int(input('Enter Option:\n1. Enter details:\n2. Display details\n3. Terminate:\n'))


	if a==1:
		id =  int(input('Enter ID of Student: ')))
		name = input('Enter Name of Student: ')
		age = int(input('Enter Age of Student: '))
		grade = input('Enter grade of student: ')
		read_data(id,name,age,grade)
	
	elif a==2:
		print (dat_list)

	
	elif a==3:
		break