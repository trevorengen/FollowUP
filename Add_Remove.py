import customer_class
import sqlite3
from db_strut import *


# Function to input new customer class
# into the SQLite3 database
def input_new():
	name = input('Enter customers full name.\n')
	phone = input('Enter customers phone number.\n')
	purchase = input('Enter product purchased.\n')
	date = input('Enter date to be delivered OR if take with purchased date.\n')

	# Now creating the customer class instance and appending it to the customer database.
	sql_command = """INSERT INTO emp (cust_name, phone_num, purchase, del_date) VALUES (?, ?, ?, ?);"""
	crsr.execute(sql_command, (name, phone, purchase, date))
	connection.commit()


# Removes a customer from the SQLite3 database
# may bolster functionality later so it can also
# be used to remove after a customer has been
# followed up with.
def remove_cust():
	cust_id = input('Enter customer ID# to be removed:\n')
	sql_command = "DELETE FROM emp WHERE cust_id = ?";
	crsr.execute(sql_command, (cust_id))
	connection.commit()
