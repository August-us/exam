from collections import defaultdict


for K in range(int(input())):
    n,k =  [int(i) for i in input().split(' ')]
    capacity =  [int(i) for i in input().split(' ')]
    realtion = defaultdict(set)
    for _ in range(n-1):
        a,b = [int(i) for i in input().split(' ')]
        realtion[a].add(b)
        realtion[b].add(a)

    last = set(range(1, 1+n))

    memory = {}
    def find_max_capacity(last, k):
        if len(last) < k:
            return -float('inf')
        key = (tuple(sorted(last)), k)
        if key in memory:
            return memory[key]
        if k == 1:
            memory[key] =  max(map(lambda x:capacity[x-1], last))
        else:
            memory[key] = -float('inf')
            for i in last.copy():
                last.remove(i)

                tmp = set()
                for j in realtion[i]:
                    if j in last:
                        last.remove(j)
                        tmp.add(j)
                memory[key] = max(find_max_capacity(last.copy(), k-1)+capacity[i-1] ,memory[key])
                last = last.union( tmp)

        return memory[key]
    res = find_max_capacity(last, k)
    if res == -float('inf'):
        print(-1)
    else:
        print(res)



'''
1
5 2
2 3 1 5 4
1 2
1 3
1 4
1 5

1
5 1
2 4 5 1 3
1 2
1 3
1 5
3 4
'''

