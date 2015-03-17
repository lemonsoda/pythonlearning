import random
import os
linecount=0
filelen=0
position=0

f = open("data.txt")
f.seek(-1,2)
filelen=position = f.tell()
print 'filelen =',filelen
while linecount<10:
    if filelen-100>=0:
        f.seek(-100,1)
        line=f.read(100)
        print "line =",line
        f.seek(-100,1)
        #postion-=100;
        for ch in line[::-1]:
            if ch=='\n':
                linecount+=1
                position-=1
            if position==10:
                break

print "position =",position
f.seek(position,0)
print f.read()
f.close()

                    
                
                
