A=list(map(int,input().strip().split(' ')))
B=list(map(int,input().strip().split(' ')))

re=-1
if A[0]>A[1]:
    re=0
if A[-1]<A[-2]:
    re=len(A)-1
if re==-1:
    for i in range(len(A)):
        if min(A[i-1:i+2])==A[i] or max(A[i-1:i+2]):
            re=i
            break
B=sorted(B,reverse=True)
flag=-1
for i in range(len(B)):
    if B[i]>A[re-1] and B[i]<A[re+1]:
        falg=i

if flag==-1:
    print('NO')

else:
    A[re]=B[flag]
    print(' '.join(map(str,A)))

"""
题目描述：A数组是一个大致升序的数组，只有一个元素影响了严格升序，然后从B中挑选一个最大元素替换之，使数组A满足升序
输入：数组A，数组B
代码完成之后未处理所有逻辑情况
"""