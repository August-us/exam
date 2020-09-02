"""
给定一个数组，求出所有的的前项差最大公约数，要求是正数
"""


n=int(input())
A=[int(i) for i in input().split(' ')]
for i in range(1,n):A[i-1]=A[i]-A[i-1]


def gcd(a, b):
    while a:
        a,b= b%a ,a
    return b

def main():
    cur = A[0]
    for i in range(1,n-1):
        if A[i]<=0:
            return -1
        cur=gcd(cur,A[i])
    return cur

print(main())



'''
4
1 3 7 15
'''
