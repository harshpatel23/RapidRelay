#!/home/tanay/Projects/BugBox/venv/bin/python

import pymysql
import socket
import zlib
import base64
import json
import traceback
import time
from threading import Thread
import os


host = 'www.google.com'
server = 'localhost'
username = 'root'
password = ''
database = 'bugbox_db'
cursorclass = pymysql.cursors.DictCursor
compressed_files_dir = 'compressed_files'
raw_files_dir = 'raw_files'
cloud_url = ''


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
	except Exception as e:
		traceback.print_exc()
	return False


def compress_data_to_file_from(table):
	print('compressing', table)
	db = pymysql.connect(server, username, password, database, cursorclass=cursorclass)
	cursor = db.cursor()

	# 1. extract data
	query = f'select * from {table};'
	# print(query)
	try:
		cursor.execute(query)
		results = cursor.fetchall()
		if not results:
			return

		# print(results)
		ids = [x['id'] for x in results]
		# print(ids)
		# print('after')

		# 2. compress and encode data
		results = json.dumps(results)
		results = bytes(results, 'utf-8')
		current_time = str(time.time()).replace('.', '_')
		with open(f'{raw_files_dir}/{table}_{current_time}', 'wb') as bin_file:
			bin_file.write(results)


		# print('json data', results)
		compressed = base64.b64encode(zlib.compress(results, 9))
		# print(compressed, type(compressed))

		with open(f'{compressed_files_dir}/{table}_{current_time}', 'wb') as bin_file:
			bin_file.write(compressed)

		# decompress in cloud
		# decompressed = zlib.decompress(base64.b64decode(compressed))
		# print(decompressed, type(decompressed))
		#
		# decompressed = json.loads(decompressed)
		# print(decompressed)

		# 3. delete data from db
		ids = ", ".join([str(x) for x in ids])
		delete_query = f'delete from {table} where id in ({ids});'
		# print(delete_query)
		cursor.execute(delete_query)
		db.commit()

	except Exception as e:
		traceback.print_exc()
		db.rollback()

	db.close()


def is_already_running():
	db = pymysql.connect(server, username, password, database, cursorclass=cursorclass)
	cursor = db.cursor()

	query = 'select value from locks where flag = 1;'
	cursor.execute(query)
	results = cursor.fetchall()

	if results[0]['value'] == 'false':
		return False
	else:
		return True


Threads = []
for table in ['agriculture_data', 'air_quality_data', 'weather_data']:
	process = Thread(target=compress_data_to_file_from, args=[table])
	process.start()
	Threads.append(process)

# check internet connection
if is_connected(host) and not is_already_running():

	# set flag
	db = pymysql.connect(server, username, password, database, cursorclass=cursorclass)
	cursor = db.cursor()
	query = 'update locks set value = "true" where flag = 1;'
	cursor.execute(query)
	db.commit()

	# if connected, send files one by one to the cloud

	print('connected')

	for filename in os.listdir(compressed_files_dir):
		print(filename)
		# send file to cloud
		pass

	# flag off
	query = 'update locks set value = "false" where flag = 1;'
	cursor.execute(query)
	db.commit()

else:
	# else don't do anything
	print('not connected or already running')
	pass
