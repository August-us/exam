# def dijkstra(graph,src, end):
#     if graph is None:
#         return None
#     nodes = [i for i in range(len(graph))]
#     visited=[]
#     if src in nodes:
#         visited.append(src)
#         nodes.remove(src)
#     else:
#         return None
#     distance={src:0}
#     for i in nodes:
#         distance[i]=graph[src][i]
#     # print(distance)
#     path={src:{src:[]}}
#     k=pre=src
#     while nodes:
#         temp_k=k
#         mid_distance=float('inf')
#         for v in visited:
#             for d in nodes:
#                 new_distance = graph[src][v]+graph[v][d]
#                 if new_distance < mid_distance:
#                     mid_distance=new_distance
#                     graph[src][d]=new_distance
#                     k=d
#                     pre=v
#         if k != src and temp_k == k:
#             break
#         distance[k]=mid_distance
#         path[src][k]=[i for i in path[src][pre]]
#         path[src][k].append(k)
#         visited.append(k)
#         nodes.remove(k)
#     return distance[end]


def dijkstra(mgraph, start, end):
    passed = [start]
    nopass = [x for x in range(len(mgraph)) if x != start]
    dis = mgraph[start]

    while len(nopass):
        idx = nopass[0]
        for i in nopass:
            if dis[i] < dis[idx]: idx = i

        nopass.remove(idx)
        passed.append(idx)

        for i in nopass:
            if dis[idx] + mgraph[idx][i] < dis[i]: dis[i] = dis[idx] + mgraph[idx][i]
    return dis[end]

n, m, T = [int(i) for i in input().split(' ')]
graph = [[float('inf') if i!=j else 0 for i in range(n)] for j in range(n)]
for i in range(m):
    s,e,d = [int(i) for i in input().split(' ')]
    graph[s-1][e-1] = d
dis = dijkstra(graph, 0, n-1)
dis += dijkstra(graph, n-1, 0)
print(dis*T)

'''
5 5 3
1 2 1
2 3 1
3 5 1
5 1 1
4 5 1
'''