# M=input()
# A=[int(i) for i in raw_input().split(' ')]

def f(start,n):
    if n==0:
        return reduce(lambda x,y:x*y, [1-a for a in A[start:]],1)

    if len(A)-start==n:
        return reduce(lambda x,y:x*y,A[start:],-1)

    else:
        return A[start]*f(start+1,n-1)+(1-A[start])*f(start+1,n)


# print f(0,0),f(0,1),f(0,2)

def ext_euclid(a, b):
    old_s,s=1,0
    old_t,t=0,1
    old_r,r=a,b
    if b == 0:
        return 1, 0, a
    else:
        while(r!=0):
            q=old_r//r
            old_r,r=r,old_r-q*r
            old_s,s=s,old_s-q*s
            old_t,t=t,old_t-q*t
    return old_s%b

print(ext_euclid(4,998244353))
print(998244353%-249561088)
print(748683265*4 %998244353 )
print(748683265*4 //998244353 )


