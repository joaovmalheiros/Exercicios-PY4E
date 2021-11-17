import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
#encode() converts from unicode to UTF-8
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    #end of file when i got no data back:
    if(len(data) < 1):
        break
    #Otherwise, print de data:
    print(data.decode())
mysock.close()
