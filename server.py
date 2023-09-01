import socket
import sys


host, port = '127.0.0.1', int(sys.argv[1])
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind((host, port))
sock.listen()
clnt_sock, clnt_addr = sock.accept()
clnt_sock.recv(1024)

html_content = "<html><body><h1>OMG you just won 100000000$</h1><p style=\"color: blue\"><u> click here to get your price :)"
html_content += "</u></p></body></html>"
response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n" + html_content
clnt_sock.sendall(response.encode())

sock.close()