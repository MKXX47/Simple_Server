# coding: utf8
import socket
import ipaddress

buffersize = 2048
 
# create socket
s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# create bytes object
msg = str.encode("Hello")
# send message
s.sendto (msg, ("localhost", 8000))
# read message
data, (ip, port) = s.recvfrom (buffersize)
print (f"[+] Client : Data from {ipaddress.IPv4Address(ip)} is {data.decode()}")
