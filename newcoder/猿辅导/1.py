# 猿辅导笔试第一题

'''
输入N表示N节课，接下来输入N行每行输入课程的开始时间和结束时间，求最多的时候有几节课时间重了。
输入示例
4
1 4
1 2
2 3
3 4
'''
n = int(input())
res = []
for i in range(n):
    s, e  =[int(i) for i in input().split(' ')]
    res.append([s, -1])
    res.append([e, s])
res.sort(key=lambda x:x[0])

maxk = k = 0
for i in res:
    if i[1]==-1:
        k+=1
    else:
        k -=1
    maxk = max(k, maxk)

print(maxk)
