n,p,q=[int(i) for i in raw_input().split(' ')]
scores=[int(i) for i in raw_input().split(' ')]
res=0
for i in scores:
    res+=p*i


def gcd(a, b):
    while a:
        a,b= b%a ,a
    return b

def ext_euclid(a, b):
    old_s,s=1,0
    # old_t,t=0,1
    old_r,r=a,b
    if b == 0:
        return 1, 0, a
    else:
        while(r!=0):
            q=old_r//r
            old_r,r=r,old_r-q*r
            old_s,s=s,old_s-q*s
            print(r,old_s)
            # old_t,t=t,old_t-q*t
            # r=as+bt
    # return old_s, old_t, old_r
    return old_s%b

f=gcd(res,q)
res/=f
q/=f
print(ext_euclid(4,998244353))





'''
3 1 2
8 8 8
'''
