def if_record_exists(datalist,id):
     for x in datalist:
         if id == x['id']:
             return True
     return False

def readdata(datalist):
       datadict={}
       datadict['id'] = int(input('Enter id of Student: '))
       '''for x in datalist:
             if datadict['id'] in x.values():
                  print ('Student already exists')
                  return False'''
       if if_record_exists(datalist,datadict['id']):
             print ('Student already exists. Please enter a different ID.')
             return  False         
       datadict['name'] = input('Enter name of Student: ')
       datadict['age'] = int(input('Enter Age of Student: '))
       datadict['grade'] = input('Enter grade of student: ')
       return datadict

def display(datalist):
    for x in datalist:
      print("________________________________")
      print("ID:%d\nNAME:%s\nAGE:%d\nGRADE:%s\n" % (x['id'],x['name'],x['age'],x['grade']))


def delete_student(datalist,id):
          count = 0
          
          if not if_record_exists(datalist,id):
                print('Student record does not exist. Please enter a different ID.')
                return
          for x in datalist:
           if x['id'] == id:
             del datalist[count]
             break
           count = count+1

def sort_students(datalist):
         n = len(datalist)
         for i in range(0,n-1):
             for j in range(0,n-1-i):
                if datalist[j]['id'] > datalist[j+1]['id']:
                     datalist[j],datalist[j+1] = datalist[j+1], datalist[j]                          
                


def search_student(datalist,id):					   
                 if not if_record_exists(datalist,id):
                    print('Student record does not exist. Please enter a different ID.')
                 for x in datalist:
                     if x['id'] == id:
                        print('Record with ID %d is: ' %(id))
                        print('_____________________')
                        print('ID:%d\nNAME:%s\nAGE:%d\nGRADE:%s\n' %(x['id'],x['name'],x['age'],x['grade']))         				  

				
def main_func():
      datalist=[]
      while True:
            opt=int(input("""
                 1. Add Record
                 2. Display Record
                 3. Delete Record
                 4. Sort Record
                 5. Search Record
                 6. Exit\n Enter your Option: """))
            if opt==1:
                  data=readdata(datalist)
                  if data==False:
                       continue
                  datalist.append(data)
            elif opt==2:
                      display(datalist)
            elif opt==3:
                  id=int(input("Enter the id to delete:"))
                  delete_student(datalist,id)
            elif opt==4:
                 sort_students(datalist)
                 display(datalist)
            elif opt == 5:
                 id = int(input('Enter id to be searched: '))
                 search_student(datalist,id)
            else:
                break


main_func()
