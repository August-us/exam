from functools import reduce
from scipy.special import comb,factorial
from math import factorial

def catalan(n):
    return int(comb(2*n,n)/(n+1))


def catalan1(n):
    return int(reduce(lambda x,y:x*(n+y)/y,range(2,n+1),1))

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result = result * i
    return result

def factorialArray(arr):
    arr=[1]+arr
    tmp=1
    res=[]
    for i in range(1,len(arr)):
        for j in range(arr[i-1]+1,arr[i]+1):
            tmp*=j
        res.append(tmp)
    return res

def comb(n,k):
    # 求阶乘可能会溢出，还可以使用C_n^k=C_{n-1}^{k-1}+C_{n-1}^k来计算
    if k>n/2:
        k=n-k
    res=factorialArray([k,n-k,n])
    return res[2]//res[1]//res[0]

def perm(n,m):
    res=factorialArray([n-m,n])
    return res[1]//res[0]

if __name__ == '__main__':
    print(comb(5,2))
    res=factorial(10)
    print(res*res*100*11**3)
    print(catalan1(10))
    print(catalan(10))