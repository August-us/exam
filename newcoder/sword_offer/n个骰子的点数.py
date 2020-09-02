def getNums(n, i):
    if n==i or 6*n==i:
        return 1
    if n>i or i >6*n:
        return 0
    res=0
    for j in range(1,7):
        res+=getNums(n-1,i-j)
    return res


def getProbability(n,s):
    nums=[0]*(5*n+1)
    for i in range(n,6*n+1):
        nums[i-n]=getNums(n,i)
    sums=sum(nums)
    k=n
    for i in nums:
        print('value=%d,probability=%f'%(k,i/sums))
        k+=1

def dp(n):
    nums=[0,1,1,1,1,1,1]
    for k in range(2,n+1):
        tmp = [0] * (6 * k + 1)
        for i in range(k,k+6):
            tmp[i]=sum(nums[:i])
        for i in range(k+6,6*k+1):
            tmp[i]=sum(nums[i-6:i])
        nums=tmp
    return nums


print(dp(3))
