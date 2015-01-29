import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in ['Michael', 'Tracy', 'Sarah']:
    s.sendto(data, ('www.lemonconey.com', 8089))
    print s.recv(1024)
s.close()
