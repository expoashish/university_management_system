import os,csv,datetime
global file_name,main,data

file_name="university.csv"


f = open(file_name, "r")
main = f.read()
main = main.split('\n') # split data 
main = list(filter(None, main))  #filter  list
print(main)
class manage():
	roll_no,std_class,dob = 0,0,0
	name,address="",""
	def __init__(self):
		self

#  ALL FUNCTION FOR THIS MANAGEMENT

	def file_write(self,list_data):
		f = open(file_name, "w")
		all_data = str()
		for data in list_data:
			all_data += data+'\n'
		f.write(all_data)
		f.close()
		return True

	def std_show(self):
		for data in main:
			data = data.split(',')
			print("Roll_no  : ",data[0])
			print("Student Name : ",data[1])
			print("Class of Student : ",data[2])
			print("DOB OF Student : ",data[3])
			print("Student Address :",data[4])

	def std_add(self):
		roll_no=int(input("Enter Roll_no : "))
		name=input("Enter Name of the Student : ")
		std_class=int(input("Enter Class of the Student : "))
		dob=input("Enter DOB of the Student :")
		address=input("Enter Address of the Student : ")

		data = str(roll_no) +','+ name+','+ str(std_class)+','+ dob+','+ address+'\n'
		
		f = open(file_name, "a")
		f.write(data)
		f.close()
		print("Student Added successfully")	

	def std_edit(self,sc):
		print("Student Roll_no :",sc)
		new_name=input("Enter Name of the Student : ")
		new_class=input("Enter Class of the Student : ")
		new_dob=input("Enter DOB of the Student : ")
		new_address=input("Enter Address of the Student : ")
		value= str(sc)+","+new_name +','+ new_class+','+ new_dob+','+ new_address
		for data in main:
			split_data=data.split(',')
			if sc == split_data[0]:
				main[main.index(data)] = value
				self.file_write(main)
				print('Successfully Updated')
				return True
		print('Try Again')



	def std_remove(self,Roll):
		for data in main:
			roll_n = data.split(',')[0]
			if(roll_n ==Roll ):
				main.remove(data)
				break
		if(self.file_write(main)):
			print('Student information Successfully Delleted')
		else:
			print('please try again')		

	def std_search(self,roll_no):
		for list_data in main:
			split_data= list_data.split(',')
			if roll_no == split_data[0]:
				print("Roll_no  : ",split_data[0])
				print("Student Name : ",split_data[1])
				print("Class of Student : ",split_data[2])
				print("DOB OF Student : ",split_data[3])
				print("Student Address :",split_data[4])

				return True

		print("Try again!!!")	

				
	def search_roll_no(self,roll_no):
		for list_data in main:
			split_data = list_data.split(',')
			if roll_no == split_data[0]:
				return True

		return False

call=manage()

print("""
	>>>>>>>>>>>>>>>>>>>>Welcome To Expo University Management<<<<<<<<<<<<<<<<<<<<<
	1.=List of All student
	2.=Add New Student
	3.=To Edit Student
	4.=To Remove Student
	5.=To Search Student
	6.=Exit Now


	""")

try:
	user_input=int(input("Enter (1-6) option for any operation :"))
except ValueError:
	print("\nThat's not true")
else:
	print("\n ")



if user_input==1:
	call.std_show()

elif (user_input==2):
	call.std_add()

elif (user_input==3):
	roll=input("Enter Student Roll_no for edit : ")	
	if call.search_roll_no(roll):
		call.std_edit(roll)
	else:
		print("Incorrect Roll_no ?????")
		
elif (user_input==4):
	roll1=input("Enter Roll_no to remove from list :")
	f=open(file_name,"r")
	read=f.read()
	if roll1 not in read:
		print("Incorrect Roll_no ?????")

	else:
		call.std_remove(roll1)

elif (user_input==5):
	roll2=input("Enter Roll_no for search more information :")
	if call.search_roll_no(roll2):
		call.std_search(roll2)
	else:
		print("Incorrect Roll_no ?????")


elif (user_input==6):
	print("Thankyou sir for using Expo University Management ")
	quit()

else:
	print("Incorrect Option?????")


call=manage()
 		