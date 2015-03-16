import string

class BigNumber:
    def __init__(self,numberString):
        self.__numberString=numberString[::-1]

    def __repr__(self):
        return self.__numberString[::-1]
    def __add__(self,other):
        result=list();
        maxlen=max(len(self.__numberString),len(other.__numberString))
        i=0
        carry=0
        while i<maxlen:

            
            valL=0
            valR=0
            if i<len(self.__numberString):
                valL=string.atoi(self.__numberString[i:i+1])
                
            if i<len(other.__numberString):
                valR=string.atoi(other.__numberString[i:i+1])
            #print self.__numberString[i:i+1],'valL=',valL,other.__numberString[i:i+1],'valR=',valR
            addVal=valL+valR+carry
            result.append(addVal%10)
            carry=addVal/10
            if(carry==0 and addVal==0):
                break
            i+=1
        return BigNumber(''.join(str(i) for i in result)[::-1])

print __name__

if __name__=="__main__":

    bigNumber=BigNumber("432432543548758457843758437587438573857348579432752934729374239874932875387532975329472937532984729357329759327532847329749327493274932")
    #print bigNumber
    bigNumber2=BigNumber("2345978237598237598475982758094725097508290385709438759275984275927592759743295793275927592759759732587492759275943275943759732954")
    #print bigNumber2
    s = bigNumber+bigNumber2
    print s
    
