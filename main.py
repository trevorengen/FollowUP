""" 
	My first program I built in order to help me keep 
	my follow up on point while working at my sales
	job. Functionality is basic but will alert you
	when a certain amount of time has passed so that
	you can follow up with a customer to ensure that
	they are happy with their purchase. Plans to increase
	functionality so it will automatically send a 
	review request to them upon users approval.

	Made by Trevor Engen 5/1/2019 8:43PM
"""

import customer_class
import sqlite3

# Database setup for sqlite3 to store customer data
# from different uses of the program
connection = sqlite3.connect('customerTable.db')
crsr = connection.cursor()
sql_command = """CREATE TABLE emp (
cust_name VARCHAR(30),
phone_num VARCHAR(20),
purchase VARCHAR(100),
del_date DATE);"""


# Function to allow new customer information
def input_new():
	name = input('Enter customers full name.\n')
	phone = input('Enter customers phone number.\n')
	purchase = input('Enter product purchased.\n')
	date = input('Enter date to be delivered OR if take with purchased date.\n')

	# Now creating the customer class instance and appending it to the customer database.
	sql_command = """INSERT INTO emp (cust_name, phone_num, purchase, del_date) VALUES (?, ?, ?, ?);"""
	crsr.execute(sql_command, (name, phone, purchase, date))
	connection.commit()


# A while loop to keep the program running until the 
# user turns it off. Will continue to allow menu selections
# until they select the end function which will terminate
# the program by changing the key to false.

key = True
while key == True:
	print('1. Enter new customer')
	print('2. Check for FollowUP\'s')
	print('3. Print full customer list')
	print('4. Remove customer')
	print('0. Terminate program')

	inp = input()

	if inp == '0':
		key = False
	
	elif inp == '1':
		input_new()
	
	elif inp == '2':
		# Add a date checker to see if the input amount of 
		# time has passed since a delivery date.
		pass
	
	elif inp == '3':
		n = 1
		crsr.execute("SELECT * FROM emp")
		ans = crsr.fetchall()
		for i in ans:
			print('\nCustomer ' + str(n) + ':')
			print(i)
			print('\n')
			n += 1

	elif inp == '4':
		chosen = input('Enter customer # from print customer screen\n')
		deli = crsr.execute("DELETE ? FROM emp")
		crsr.execute(deli, chosen)



connection.close()