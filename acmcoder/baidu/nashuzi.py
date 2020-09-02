n=input()
m=input()

A=[int(i) for i in raw_input().split(' ')]
B=[int(i) for i in raw_input().split(' ')]

def getM(m,n,A,B,already):
    res=-2**31
    if m==1:
        for i in range(len(A)):
            if i in already:
                continue
            res=max(res,A[i]-n*B[i])
    else:
        for i in range(len(A)):
            if i in already:
                continue
            already.append(i)
            res=max(A[i]+getM(m-1,n+1,A,B,already)-n*B[i],res)
            already.pop()
    return res

print getM(m,0,A,B,[])

'''
5
5
10 20 30 40 50
4 5 6 7 8
'''