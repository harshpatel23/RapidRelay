import pymysql
import socket
import zlib
import base64
import json
import traceback
from threading import Thread
import socket


host = 'www.google.com'
server = 'localhost'
username = 'root'
password = ''
database = 'bugbox_db'
cursorclass = pymysql.cursors.DictCursor


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
	db = pymysql.connect(server, username, password, database, cursorclass=cursorclass)
	cursor = db.cursor()

	# 1. extract data
	query = f'select * from {table};'
	print(query)
	try:
		cursor.execute(query)
		results = cursor.fetchall()
		print(results)
		ids = [x['id'] for x in results]
		print(ids)
		print('after')
		# 2. compress and encode data
		results = json.dumps(results)
		print('json data', results)
		compressed = base64.b64encode(zlib.compress(bytes(results, 'utf-8'), 1))
		# print(compressed)

		# decompress in cloud
		# decompressed = zlib.decompress(base64.b64decode(compressed))
		# print(decompressed, type(decompressed))
		#
		# decompressed = json.loads(decompressed)
		# print(decompressed)

		# 3. send data to cloud



		# 4. delete data from db
		ids = ", ".join([str(x) for x in ids])
		delete_query = f'delete from {table} where id in ({ids});'
		print(delete_query)
		cursor.execute(delete_query)
		db.commit()
	except Exception as e:
		traceback.print_exc()
		db.rollback()

	db.close()

def send_data_to_cloud(filename):
	s = socket.socket()             # Create a socket object
	host = socket.gethostname()     # Get local machine name
	port = 60000                    # Reserve a port for your service.
	buffer_size = 102400

	s.connect((host, port))

	f = open(filename,'rb')
	l = f.read(buffer_size)
	while (l):
	   s.send(l)
	   # print('Sent ',repr(l))
	   l = f.read(buffer_size)
	f.close()

	print('Done sending'+filename)
	s.close()
	f.close()
	s.close()


# check internet connection
Threads = []
if is_connected(host):
	# if connected
	for table in ['agriculture_data', 'air_quality_data', 'weather_data']:
		process = Thread(target=upload_data_from, args=[table])
		process.start()
		Threads.append(process)

else:
	# else don't do anything
	pass