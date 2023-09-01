import socket
import sys

hostname, port = sys.argv[1], int(sys.argv[2])
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((hostname, port))

request = "GET / HTTP/1.1\r\nHost: " + hostname + "\r\n\r\n"

sock.send(request.encode())

response = sock.recv(1024)
print(response.decode())

sock.close()