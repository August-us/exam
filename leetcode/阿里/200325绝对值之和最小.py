
n=int(input())
a1=[int(i) for i in input().split(' ')]
a2=[int(i) for i in input().split(' ')]
a3=[int(i) for i in input().split(' ')]
A=list(zip(a1,a2,a3))
pre=[a1[0],a2[0],a3[0]]
minsum=[0,0,0]
preSum=[0,0,0]


for i in range(1,n):
    for row in range(3):
        minsum[row]=min([preSum[num]+abs(A[i][row]-A[i-1][num]) for num in range(3)])
    preSum=minsum.copy()
print(min(minsum))

'''
5
5 9 5 4 4
4 7 4 10 3
2 10 9 2 3
'''

