

schools=['A','B','C','D','E']
persons=['A','B','C','D','E']

def verify(person,school,rank):

    if school=='E':
        return not(rank==2 or rank==3)
    
    if person=='A':
        return (school=='E' and rank==1)

    if person=='B':
        return (school=='B' and rank=2)

    if person=='C':
        return (school=='A' and rank==5)

    if person=='D':
        return (school=='C' and rank!=1)

    if person=='E':
        return (school=='D' and rank==1)

