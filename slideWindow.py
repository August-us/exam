from queue import Queue

n,m,k=[int(i) for i in input().split(' ')]
A=[int(i) for i in input().split(' ')]
q=Queue(m)
q.put(1)
pre=1
newValue=A[0]
for i in range(m-1):
    maxi=max(A[pre:pre+k])
    newValue+=maxi
    pre+=A[pre:pre+k].index(maxi)+1
    q.put(pre)

maxValue=newValue

while True:
    try:
        head=q.get()
        maxi = max(A[pre:pre + k])
        newValue+=maxi-A[head-1]
        pre += A[pre:pre + k].index(maxi) + 1
        maxValue=max(maxValue,newValue)
        q.put(pre)
    except ValueError:
        break
print(maxValue)

'''
题目描述：输入三个数，分别表示序列长度，选择的数字个数m，以及数据间隔k，然后输入这个序列，从序列中找出最大的m个数，但是每相邻的两个数之间
下标之差不能超过k，能够取到的最大值，以下示例输出6

6 2 2
4 1 2 3 1 2
'''