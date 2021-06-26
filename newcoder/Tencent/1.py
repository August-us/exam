from collections import defaultdict

n = int(input())
for i in range(n):
    res = 0

    lgth = int(input())
    descend = [1 for i in range(lgth)]
    ascend = [1 for i in range(lgth)]

    cur = [int(i) for i in input().split(' ')]
    index = defaultdict(list)
    for id,n in enumerate(cur):
        index[n].append(id)
        for j in range(id):
            if cur[j]>n:
                descend[id] = max(descend[id], descend[j]+1)

    for id in range(lgth-1, -1, -1):
        for j in range(lgth-1, id, -1):
            if cur[j]>cur[id]:
                ascend[id] = max(ascend[id], ascend[j] + 1)
        index[cur[id]].pop()
        if index[cur[id]]:
            print(descend[index[cur[id]][-1]], ascend[id])
            res = max(res, 2*min(descend[index[cur[id]][-1]],ascend[id]))
            print(cur)
            print(ascend)
            print(descend)
    print(res)





'''
3
9
5 4 3 2 1 2 3 4 5
5
1 2 3 4 5
14
87 70 17 12 14 86 61 51 12 90 69 89 4 65

'''