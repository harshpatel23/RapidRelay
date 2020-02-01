import socket                   # Import socket module

s = socket.socket()             # Create a socket object
host = '192.168.225.70'     # Get local machine name
port = 60000                    # Reserve a port for your service.

s.connect((host, port))
s.send(str.encode("Hello server!"))

filename='sample_1.txt'
f = open(filename,'rb')
l = f.read(102400)
while (l):
   s.send(l)
   # print('Sent ',repr(l))
   l = f.read(102400)
f.close()

print('Done sending')
s.send(str.encode('Thank you for connecting'))
s.close()

f.close()
print('Successfully sent the file')
s.close()
print('connection closed')
