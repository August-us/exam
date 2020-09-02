def main():
    n,m,t = [int(i) for i in input().split(' ')]
    if t ==0:
        print(0)
        return
    res = float('inf')
    mid = [[0,0]]
    night = [[0,0]]
    minmid = float('inf')
    for _ in range(n):
        mid.append([int(i) for i in input().split(' ')])
        minmid = min(minmid, mid[-1][0])
    mid.sort(key=lambda x:x[1])
    for _ in range(m):
        night.append([int(i) for i in input().split(' ')])
    night.sort(key=lambda x:x[1])
    print(mid)
    print(night)
    if mid[-1][1] + night[-1][1] < t:
        print(-1)
        return
    for i in range(len(mid)-1, -1, -1):
        if mid[i][1] + night[-1][1] < t:
            break
        for j in range(len(night)-1, -1, -1):
            if mid[i][1] + night[j][1] >=t:
                res = min(res ,mid[i][0] + night[j][0])
            else:
                break
        if mid[i][0]==minmid:
            break
    print(res)


def deleteSupported(array):
    array.sort(key=lambda x:x[1],reverse=True)
    newArray = []
    pre = float('inf')
    for item in array:
        if item[0] < pre:
            pre = item[0]
            newArray.append(item)
    return newArray  # 注意，这里已经是倒序了，所以后面循环不需要倒序

def main():
    n,m,t = [int(i) for i in input().split(' ')]
    if t ==0:
        print(0)
        return
    res = float('inf')
    mid = [[0,0]]
    night = [[0,0]]
    for _ in range(n):
        mid.append([int(i) for i in input().split(' ')])
    mid = deleteSupported(mid)
    for _ in range(m):
        night.append([int(i) for i in input().split(' ')])
    night = deleteSupported(night)

    if mid[0][1] + night[0][1] < t:
        print(-1)
        return
    i, j = len(mid)-1, 0
    while j<len(night) and i>=0:
        if mid[i][1] + night[j][1] >= t:
            res = min(res, mid[i][0] + night[j][0])
            j+=1
        else:
            i -=1
    print(res)


def main1():
    n,m,t = [int(i) for i in input().split(' ')]
    if t ==0:
        print(0)
        return
    res = float('inf')
    mid = [[0,0]]
    night = [[0,0]]
    for _ in range(n):
        mid.append([int(i) for i in input().split(' ')])
    mid = deleteSupported(mid)
    for _ in range(m):
        night.append([int(i) for i in input().split(' ')])
    night = deleteSupported(night)

    if mid[0][1] + night[0][1] < t:
        print(-1)
        return
    for i in range(len(mid)):
        if mid[i][1] + night[0][1] < t:
            break
        for j in range(len(night)):
            if mid[i][1] + night[j][1] >=t:
                res = min(res ,mid[i][0] + night[j][0])
            else:
                break
    print(res)

if __name__ == '__main__':
    main1()
'''
5 1 9
9 1
4 9
3 1
2 3
6 5
9 8


1 1 0
3 1
2 1

3 3 10
1 1
2 5
3 7
2 4
8 8
6 9

2 1 4
3 1
2 1
1 2


2 2 9
5 9
4 8
5 9
3 9
'''

