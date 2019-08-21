import math
while True:
    try:
        n,a,x=[int(i) for i in input().strip().split()]
        A=list(map(int,input().strip().split()))
        bugtime=sum(A)

        if bugtime<=x*a*60:
            print(math.ceil(bugtime/a))
        elif bugtime< 60*(8-x)+a*x*60:
            print(bugtime-60*(a-1))
        else:
            print(0)
    except:
        break

'''
8 2 8
60 60 60 60 60 60 60 60
4 3 3
333 77 100 13
'''