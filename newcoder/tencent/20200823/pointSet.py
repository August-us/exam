from collections import defaultdict

graph = defaultdict(set)
alread = defaultdict(lambda :0)
res = 0
n , m =[int(i) for i in input().split(' ')]
for i in range(m):
    s, e = [int(i) for i in input().split(' ')]
    graph[s].add(e)
    graph[e].add(s)

for k,v in graph.items():
    res += alread[tuple(v)]
    alread[tuple(v)] += 1

print(res)

'''
4 3
1 2
2 3
2 4

6 5
1 3
2 3
3 5
4 5
5 6
'''