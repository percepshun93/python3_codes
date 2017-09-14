#Initialize empty list
dat_list = []

while True:
	a = int(input('Enter Option:\n1. Enter details:\n2. Display details\n3. Terminate:\n'))


	if a==1:
		name = input('Enter name of Student: ')
		age = int(input('Enter Age of Student: '))
		grade = input('Enter grade of student: ')
		dict1 = {'Name of Student':name, 'Age of student':age,'Grade of student':grade}
		dat_list.append(dict1)

	
	elif a==2:
		print(dat_list)

	
	elif a==3:
		break