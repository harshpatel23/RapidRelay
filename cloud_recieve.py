import socket                   # Import socket module
import time

port = 60000                    # Reserve a port for your service.
s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
s.bind(('0.0.0.0', port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.
buffer_size = 102400

print('Server listening....')

while True:
	conn, addr = s.accept()     # Establish connection with client.
	print('Got connection from', addr)
	file_name = "recieved_file_"+str(int(time.time()))+".txt"
	with open(file_name, 'wb+') as f:
		while True:
			data = conn.recv(buffer_size)
			if not data:
				break
			# write data to a file
			f.write(data)

	print("Recieved file "+file_name)

	# decompress file
	# TODO
	# decompress in cloud
	# decompressed = zlib.decompress(base64.b64decode(compressed))
	# print(decompressed, type(decompressed))
	#
	# decompressed = json.loads(decompressed)
	# print(decompressed)

	# parse data and put it in sql
	# TODO

	# remove compressed file
	# TODO

	conn.close()