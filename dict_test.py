flag = 0
dat_list = []

while flag<5:
	a = input('Enter name: ')
	b = input('Enter age: ')
	c = input('Enter grade: ')
	dict1 = {'Name':a,'Age':b,'Grade':c}
	dat_list.append(dict1) 
	flag = flag+1


print(dat_list)
	
	
