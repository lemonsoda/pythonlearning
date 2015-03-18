import itertools

schools=['A','B','C','D','E']
answers={'A':'E','B':'B','C':'A','D':'C','E':'D'}


def verify(person,perm):
    school=answers[person]
    rank=''.join(perm).find(school)+1
    if person=='A':
        return (school=='E' and rank==1)

    if person=='B':
        return (school=='B' and rank==2)

    if person=='C':
        return (school=='A' and rank==5)

    if person=='D':
        return (school=='C' and rank!=1)

    if person=='E':
        return (school=='D' and rank==1)
    

maybe=itertools.permutations(schools)

for val in maybe:
    if val[2-1]=='E' or val[3-1]=='E':
        #print val
        continue
    success=True
    rightSchools=val[:2]
    wrongSchools=val[2:]
    for rs in rightSchools:
        if not verify(rs,val):
            success=False
    for ws in wrongSchools:
        if verify(ws,val):
            success=False
    if success:
        print 'Order is:',val
        print rightSchools,'said truth.'
    

