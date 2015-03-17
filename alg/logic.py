
players=['A','B','C','D','E','F']
persons=['JIA','YI','BING','DING']
champion=None

def verify(person,champion):

    if person=='JIA':
        return champion=='A' or champion=='B'
    if person=='YI':
        return not (champion=='C')
    if person=='BING':
        return not (champion=='D' or champion=='E' or champion=='F')
    if person=='DING':
        return champion=='D' or champion=='E' or champion=='F'


for player in players:
    rightCount=0
    currentPerson=None
    for person in persons:
        isRight=verify(person,player)
        #print 'isRight=%s,%s said %s is champion.'%(isRight,person,player)
        if isRight:
            rightCount+=1
            currentPerson=person

    if rightCount==1:
        print player,'is champion',currentPerson,'said is truth.'


        
