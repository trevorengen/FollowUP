import customer_class
import sqlite3
from db_strut import *
import time
from datetime import date, timedelta, datetime


# Function to input new customer class
# into the SQLite3 database
# TODO make it so the customerID
# starts back at one if the table
# is empty.
def input_new():
	name = input('Enter customers full name.\n')
	phone = input('Enter customers phone number.\n')
	purchase = input('Enter product purchased.\n')
	date = input('Enter date to be delivered OR if take with purchased date. (MM-DD-YYYY)\n')

	# Now creating the customer class instance and appending it to the customer database.
	sql_command = """INSERT INTO emp (cust_name, phone_num, purchase, del_date) VALUES (?, ?, ?, ?);"""
	crsr.execute(sql_command, (name, phone, purchase, date))
	connection.commit()


# Removes a customer from the SQLite3 database
# TODO Bolster functionality so it can also
# be used to remove after a customer has been
# followed up with.
def remove_cust():
	cust_id = input('Enter customer ID# to be removed:\n')
	sql_command = "DELETE FROM emp WHERE cust_id = ?";
	crsr.execute(sql_command, (cust_id))
	connection.commit()

# Function to check date vs customers delivery date
# to check if they require a follow up to ensure
# everything went smoothly.
def follow_up():
	
	today = date.today()
	sql_command = "SELECT del_date FROM emp"
	sql_commandt = "SELECT cust_id FROM emp"
	crsr.execute(sql_command)
	dates = [crsr.fetchall()]
	connection.commit()
	
	print('Follow up with the following customers:\n')

	for date_list in dates:
		for cust_date in date_list:
				# Changes the delivery date in SQL into a proper
				# date time object then adds 14 days and checks
				# if today is past that date. If so
				# informs user to check up with the customer.
				non_tup = str(cust_date)
				cust_del_date = datetime.strptime(non_tup, "('%m-%d-%Y',)").date()			
				followup_date = cust_del_date + timedelta(days=14)
				del_date = non_tup
				if followup_date <= date.today():
					crsr.execute("SELECT cust_name FROM emp WHERE del_date=?", (cust_date))
					cust_name = crsr.fetchall()

					crsr.execute("SELECT purchase FROM emp WHERE del_date=?", (cust_date))
					cust_purchase = crsr.fetchall()

					crsr.execute("SELECT phone_num FROM emp WHERE del_date=?", (cust_date))
					cust_number = crsr.fetchall()
					
					stripped_name = ''
					stripped_purchase = ''
					stripped_number = ''

					for i in cust_name:
						i_str = str(i)
						stripped_name += i_str.strip('\'()[]\',')

					for i in cust_purchase:
						i_str = str(i)
						stripped_purchase += i_str.strip('\'()[]\',')

					for i in cust_number:
						i_str = str(i)
						stripped_number += i_str.strip('\'()[]\',')


					print('Name: {} Purchase: {} Phone #: {}'.format(stripped_name, stripped_purchase, stripped_number))












