n,m=[int(i) for i in input().split(' ')]
A=sorted([int(i) for i in input().split(' ')])
q=int(input())


# for i in range(q):
#     num=int(input())
#     res=sum(A[:num%m])*(num//m+1)
#     for k in range(1,num//m+1):
#         res+=k*sum(A[num-k*m:num-(k-1)*m])
#     print(res)


for _ in range(q):
    num=int(input())
    result=0
    count=0
    i=num-1
    while i>=0:
        for j in range(m):
            if i-j>0:
                result+=A[i-j]*count
            count+=1
            i=i-m
    print(result)

for i in range(1,n):
    A[i]+=A[i-1]

for i in range(m,n):
    A[i]+=A[i-m]
print(A)
for i in range(q):
    num=int(input())
    print(A[num-1])

'''
5 2
1 2 3 4 5
2
3
5
'''




