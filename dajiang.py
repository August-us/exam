def dijkstra(graph,src):
    # 判断图是否为空，如果为空直接退出
    if graph is None:
        return None
    nodes = [i for i in range(len(graph))]  # 获取图中所有节点
    visited=[]  # 表示已经路由到最短路径的节点集合
    if src in nodes:
        visited.append(src)
        nodes.remove(src)
    else:
        return None
    distance={src:0}  # 记录源节点到各个节点的距离
    for i in nodes:
        distance[i]=graph[src][i]  # 初始化
    # print(distance)
    path={src:{src:[]}}  # 记录源节点到每个节点的路径
    k=pre=src
    while nodes:
        temp_k=k
        mid_distance=float('inf')
        for v in visited:
            for d in nodes:
                new_distance = graph[src][v]+graph[v][d]
                if new_distance < mid_distance:
                    mid_distance=new_distance
                    graph[src][d]=new_distance  # 进行距离更新
                    k=d
                    pre=v
        if k != src and temp_k == k:
            break
        distance[k]=mid_distance  # 最短路径
        # 更新两个节点集合
        visited.append(k)

        nodes.remove(k)
    return distance


if __name__ == '__main__':
    while True:
        n,p,c=[int(i) for i in input().strip().split()]
        graph = [[float('inf') if i!=j else 0 for i in range(n)] for j in range(n)]
        for i in range(p):
            s, e, d = [int(i) for i in input().strip().split()]
            graph[s][e]=d
            graph[e ][s] = d
        distance= dijkstra(graph, 0)  # 查找从源点0开始带其他节点的最短路径
        result=[]
        for i in range(c):
            result.append(distance[int(input())])
        print(sum(result))
'''
2 1 1
0 1 10
1
4 5 3
0 1 15
1 2 15
0 3 50
1 3 30
2 3 10
2
1
3
'''