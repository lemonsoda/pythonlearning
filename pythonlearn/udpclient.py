import socket


for data in ['Michael', 'Tracy', 'Sarah']:
    s.sendto(data, ('www.lemonconey.com', 8089))
    print s.recv(1024)
s.close()