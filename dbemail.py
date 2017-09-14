import pymysql
import smtplib

db = pymysql.connect('localhost','root','root','Datacenter')

crs = db.cursor()

crs.execute("DROP TABLE IF EXISTS INFORMATION")

crs.execute("""CREATE TABLE INFORMATION( 
						ID INT NOT NULL,
						NAME VARCHAR(50) NOT NULL,
						AGE INT NOT NULL,
						GRADE VARCHAR(2) NOT NULL,
						PRIMARY KEY(ID)
						);""")
						
def readDat(id,name,age,grade):
	crs.execute("""INSERT INTO INFORMATION(ID,NAME,AGE,GRADE) VALUES(%d,'%s',%d,'%s')""" %(id,name,age,grade))
	db.commit()
	
def displayDat():
	crs.execute("SELECT * FROM Information;")
	data=crs.fetchall()
	for x in data:
	    print(x)
	
def deleteDat(id):
	crs.execute("DELETE FROM INFORMATION WHERE ID=%d;" %(id))
	db.commit()
	
def searchDat(id):
	crs.execute("SELECT * FROM INFORMATION WHERE ID=%d;" %(id))
	data = crs.fetchone()
	print(data)
	
def sendMail(id):
	crs.execute("SELECT * FROM INFORMATION WHERE ID=%d;" %(id))
	data = crs.fetchone()
	msg = "Student of ID: %d\nName: %s\nand Age: %d has the final term grade of: %s" %(data[0],data[1],data[2],data[3])
	print (msg)
	 
	 
	TO = 'subhasish.sarkar93@gmail.com'
	FROM = 'tempemailpython@gmail.com'
	SUB = 'Student details sent using python smtp module'
	
	mail = smtplib.SMTP('smtp.gmail.com',587) #specify the smtp mail server and port
	mail.ehlo()  #identify yourself to the server using helo() for regular, use ehlo() for extended smtp server
	
	#start ssl encryption
	mail.starttls()
	mail.ehlo()
	
	#login to your mail
	mail.login(FROM,'yahoo.com')
	
	body = '\r\n'.join([
				'TO: %s' % TO,
				'FROM: %s' % FROM,
				'SUBJECT: %s' % SUB,
				"\nStudent of ID: %d\nName: %s\nand Age: %d has the final term grade of: %s" %(data[0],data[1],data[2],data[3])
				])
	
	#send the mail to your specified mail id
	mail.sendmail(FROM,TO,body)
	print('Sent all information via email')
	mail.quit()
	
	
def main_func():
	while True:
		opt=int(input("""
					1. Add Record
					2. Display Record
					3. Delete Record
					4. Search Record
					5. Send Mail of the Record
					6. Exit\n Enter your Option: """))
		
		if opt == 1:
			id = int(input('Enter ID of student: '))
			name = input('Enter Name of student: ')
			age = int(input('Enter age of student: '))
			grade = input('Enter the grade of the student: ')
			readDat(id,name,age,grade)
		elif opt == 2:
			displayDat()
		elif opt == 3:
			id = int(input('Enter ID to be deleted: '))
			deleteDat(id)
		elif opt == 4:
			id = int(input('Enter ID to be searched: '))
			searchDat(id)
		elif opt == 5:
			id = int(input('enter id to be sent: '))
			sendMail(id)
		else:
			db.close()
			break

main_func()