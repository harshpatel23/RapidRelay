import socket                   # Import socket module
import time
import json
import zlib
import base64
import os
import pymysql


port = 60000                    # Reserve a port for your service.
s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
s.bind(('0.0.0.0', port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.
buffer_size = 102400

server = 'localhost'
username = 'root'
password = ''
database = 'bugbox_db'
cursorclass = pymysql.cursors.DictCursor

print('Server listening....')

while True:
	conn, addr = s.accept()     # Establish connection with client.
	print('Got connection from', addr)
	file_name = "received_file_"+str(int(time.time()))+".txt"
	with open(file_name, 'wb+') as f:
		while True:
			data = conn.recv(buffer_size)
			if not data:
				break
			# write data to a file
			f.write(data)

	print("Recieved file "+file_name)

	# decompress file
	with open(file_name, 'rb') as file:
		decompressed = zlib.decompress(base64.b64decode(file.read()))

	# decompress in cloud
	decompressed = json.loads(decompressed)

	# parse data and put it in sql
	# TODO
	db = pymysql.connect(server, username, password, database, cursorclass=cursorclass)
	cursor = db.cursor()

	try:
		for data in decompressed:
			if 'greenhouse_id' in data.keys():
				table = 'agriculture_data'
			elif 'SO2' in data.keys():
				table = 'air_quality_data'
			else:
				table = 'weather_data'
			columns = ', '.join(list(data.keys()))
			values = list(data.values())
			values = [str(x) for x in values]
			values = '"'+'", "'.join(values)+'"'
			query = f'insert into {table} ({columns}) values ({values});'

		db.commit()
	except:
		db.rollback()

	# remove compressed file
	os.remove(file_name)

	conn.close()
