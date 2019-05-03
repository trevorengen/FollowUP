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
from Add_Remove import input_new, remove_cust
from db_strut import *


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
		crsr.execute("SELECT * FROM emp")
		ans = crsr.fetchall()
		for i in ans:
			print(i)
			print('\n')

	elif inp == '4':
		remove_cust()

	elif inp == '5':
		pass



connection.close()