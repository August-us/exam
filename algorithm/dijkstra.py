def dijkstra(graph,src):
    '''
    :param graph: 使用邻接矩阵存储，不可达节点使用inf表示，自己之间的距离设置为0
    :param src: 源节点的编号
    :return: distance 原点到每个节点的距离，path，原点到第i个点的路径
    '''
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
                    graph[src][d] = new_distance  # 进行距离更新
                    k=d
                    pre=v
        if temp_k == k:
            break
        distance[k]=mid_distance  # 最短路径
        path[src][k]=[i for i in path[src][pre]]
        path[src][k].append(k)
        # 更新两个节点集合
        visited.append(k)
        # print(k)
        nodes.remove(k)
        # print(visited,nodes)  # 输出节点的添加过程
    return distance,path

def dijkstra_dict(graph,src):
    '''
    :param graph: 使用邻接表存储，图使用list存储，可达节点使用字典存储
    :param src: 源节点的编号
    :return: distance 原点到每个节点的距离，path，原点到第i个点的路径
    '''
    # 判断图是否为空，如果为空直接退出
    if graph is None:
        return None
    graph = [i.copy() for i in graph]

    nodes = [i for i in range(len(graph))]  # 获取图中所有节点
    visited=set()  # 表示已经路由到最短路径的节点集合
    if src in nodes:
        visited.add(src)
        nodes.remove(src)
    else:
        return None
    distance={src:0}  # 记录源节点到各个节点的距离
    for i in nodes:
        distance[i]=graph[src].get(i,float('inf'))  # 初始化
    # print(distance)
    path={src:{src:[]}}  # 记录源节点到每个节点的路径
    k=pre=src
    while nodes:
        temp_k=k
        mid_distance=float('inf')
        for v in visited:
            for d in set(graph[v].keys()) - visited:
                new_distance = distance[v]+graph[v][d]
                if new_distance < mid_distance:
                    mid_distance=new_distance
                    graph[src][d]=min(new_distance,graph[src].get(d,float('inf')))  # 进行距离更新，因为visited使用集合，可能会导致无序，以至于提前修改
                    k=d
                    pre=v
        if temp_k == k:
            break
        distance[k]=mid_distance  # 最短路径
        path[src][k]=[i for i in path[src][pre]]
        path[src][k].append(k)
        # 更新两个节点集合
        visited.add(k)
        # print(k)
        nodes.remove(k)
        # print(visited,nodes)  # 输出节点的添加过程
    return distance,path


if __name__ == '__main__':
    graph_list = [ [0, 2, 1, 4, 5, 1],
            [1, 0, 4, 2, 3, 4],
            [2, 1, 0, 1, 2, 4],
            [3, 5, 2, 0, 3, 3],
            [2, 4, 3, 4, 0, 1],
            [3, 4, 7, 3, 1, 0]]
    graph = [
        [0, float('inf'), 10, float('inf'), 30, 100],
        [float('inf'), 0, 5, float('inf'), float('inf'), float('inf')],
        [float('inf'), float('inf'), 0, 50, float('inf'), float('inf')],
        [float('inf'), float('inf'), float('inf'), 0, float('inf'), 10],
        [float('inf'), float('inf'), float('inf'), 20, 0, 60],
        [float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 0]]

    distance,path= dijkstra([[0, 10], [10, 0]], 0)  # 查找从源点0开始带其他节点的最短路径
    print(distance,path)