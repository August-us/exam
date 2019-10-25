n=int(input())
A=[int(i) for i in input().split(' ')]
pre=[1 for i in range(n)]
last=[1 for i in range(n)]
for i in range(1,n):
    pre[i] = pre[i - 1] + 1 if A[i] > A[i - 1] else 1
for i in range(n-2,-1,-1):
    last[i]=last[i+1]+1 if A[i+1]>A[i] else 1
res=1
print(pre,last)
for i in range(1,n-1):
    res=max(res,pre[i],last[i])
    if A[i+1]-A[i-1]>=2:
        res=max(res,pre[i-1]+last[i+1]+1)
    elif A[i+1]-A[i-1]==1:
        res = max(res, pre[i - 1] + last[i + 1] )
print(res)

'''
题目描述：
给定一个数字序列，最多可以改变(删除)其中一个数字，使得其中的子串是最长上升连续子串
5
3 1 2 5 4
改变5为3，输出4

4
3 7 4 8
删除7，输出3

'''