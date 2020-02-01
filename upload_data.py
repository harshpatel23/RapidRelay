import pymysql
import socket


host = 'www.google.com'
server = 'localhost'
username = 'root'
password = ''
database = ''


def is_connected(hostname):
	try:
		# see if we can resolve the host name -- tells us if there is
		# a DNS listening
		host = socket.gethostbyname(hostname)
		# connect to the host -- tells us if the host is actually
		# reachable
		s = socket.create_connection((host, 80), 2)
		s.close()
		return True
	except:
		pass
	return False


def upload_data_from(table):
	query = f'select * from table {table}'


# check internet connection
if is_connected(host):
	# if connected,
	# 1. extract and compress data
	db = pymysql.connect(server, username, password, database)
	cursor = db.cursor()
	# execute SQL query using execute() method.
	cursor.execute("SELECT VERSION()")

	# Fetch a single row using fetchone() method.
	data = cursor.fetchone()
	print ("Database version : %s " % data)


	# 2. send data to cloud
	# 3. delete data from db
else:
	# else don't do anything
	pass