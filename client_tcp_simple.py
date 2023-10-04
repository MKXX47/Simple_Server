import socket

buffersize = 2048

# create socket
s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
# connect to server
s.connect(("localhost", 8000))
# create bytes object
msg = str.encode("Hello")
# send message
s.send(msg)
# read message
data = s.recv(buffersize)
# close connection
s.close()
