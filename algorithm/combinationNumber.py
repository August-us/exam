from scipy.special import comb,factorial

def catalan(n):
    return int(comb(2*n,n)/(n+1))
print(comb(5,2))
def catalanArray(n):
    result=[1]
    for i in range(1,n+1):
        tmp=0
        for j in range(i):
            tmp+=result[j]*result[i-j-1]
        result.append(tmp)
    print(result)

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result = result * i
    return result

def factorialArray(arr):
    arr=[1]+arr
    print(arr)
    tmp=1
    res=[]
    for i in range(1,len(arr)):
        for j in range(arr[i-1]+1,arr[i]+1):
            tmp*=j
        res.append(tmp)
    return res

def comb(n,k):
    if k>n/2:
        k=n-k
    res=factorialArray([k,n-k,n])
    return res[2]//res[1]//res[0]

def perm(n,m):
    res=factorialArray([n-m,n])
    return res[1]//res[0]

print(comb(5,2))
res=factorial(10)
print(res*res*100*11**3)
