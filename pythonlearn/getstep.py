


def f(n,left):
    if n==1 or n==2:
        return 1
    if n==3:
        return 2
    if n>3 and left==3:
        return f(3,0)*f(n-3,0)
    if n>3 and left>3:
        return f(3,left-2)*f(n-2,left-2)+f(1,0)*f(n-1,left-1)

if __name__=='__main__':

    for step in range(1,11):
        print '%3d step has %10d method' % (step,f(step,step))
