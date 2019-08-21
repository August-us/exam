a=[0,1]
b=[0,1]
people=100
def dp(n):
    for i in range(1,n+1):
        if i==len(b):
            count=0
            for j in range(1,i):
                count+=b[j]+1
            exp=(count+1)/float(i)
            b.append(exp)

def suv(n):
    if n<len(a):
        return a[n]
    else:
        exp=0
        for i in range(1,n):
            exp+=suv(i)
        exp=exp/float(n)+1
        a.append(exp)
        return exp

suv(people)
# suv(people)
# print a
# print b
print (b[people])



