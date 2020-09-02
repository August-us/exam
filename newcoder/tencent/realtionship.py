from collections import defaultdict

T = int(input())
for i in range(T):
    A = []
    n = int(input())
    node_father = {}

    def getroot(node):
        if node not in node_father:
            node_father[node] = node
        elif node_father[node_father[node]] != node_father[node]:
            node_father[node] = getroot(node_father[node])
        return node_father[node]

    for j in range(n):
        edge =[int(i) for i in input().split(' ')]

        if edge[0] not in node_father:
            node_father[edge[0]] = getroot(edge[1])
        elif edge[1] not in node_father:
            node_father[edge[1]] = getroot(edge[0])
        else:
            node_father[getroot(edge[0])] = getroot(edge[1])

    res = 0
    nodenum = defaultdict(lambda: 0)
    for node in node_father:
        root = getroot(node)
        nodenum[root] += 1
        res = max(res, nodenum[root])
    print(res)


'''
2
4
1 2
3 4
5 6
1 6
4
1 2
3 4
5 6
7 8
'''