import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('www.lemonconey.com', 8087))
print s.recv(1024)
for data in ['Michael', 'Tracy', 'Sarah']:
    s.send(data)
    print s.recv(1024)
s.send('exit')
s.close()
