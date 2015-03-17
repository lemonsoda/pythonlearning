
import sys
import os
#print sys.argv


class LinkedLine():

    def __init__(self):
        self.__next=None
    def setNext(self,nextNode):
        self.__next=nextNode
    def getNext(self):
        return self.__next
    def setText(self,text):
        self.__text=text
    def getText(self):
        return self.__text
    
head=LinkedLine()
current=head
for i in range(2,11):
    node =LinkedLine()
    current.setNext(node)
    current=node
current.setNext(head)
current=current.getNext()

with open("data.txt") as f:
    while True:
        line=f.readline()
        if line:
            current.setText(line.strip())
            current=current.getNext()
        else:
            break
newStart=current
print current.getText()
current=current.getNext()
while current!=newStart:
    print current.getText()
    current=current.getNext()

current.setNext(None)

