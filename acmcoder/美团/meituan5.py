from scipy.special import comb

n,k=[int(i) for i in raw_input().split()]
A=[int(i) for i in raw_input().split()]
for i in range(k-1):
    for j in range(1,n):
        A[j]+=A[j-1]
    print(A)
print(sum(A))

'''
4 6
1 0 0 0
'''

