import socket
import ipaddress

buffersize = 2048
# create socket
s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
# bind socket to address and port
s.bind(("0.0.0.0", 8000))
# wait for connections
s.listen(0)
# accept connections forever
while True:
    conn, (ip, port) = s.accept()
    print(f"Connected to {ipaddress.IPv4Address(ip)}:{port}")

    # listen for data and reply with "Message received"
    while True:
        data = conn.recv(buffersize)
        # client finished sending message
        if not data:
            break
        print(f"[+] Serveur : Received {data.decode()}")
        msg = str.encode("[+] Serveur : Send message received")
        conn.send(msg)
    # close connection
    conn.close()
