#encoding=utf-8
#  Bellman-Ford核心算法
# 对于一个包含n个顶点，m条边的图, 计算源点到任意点的最短距离
# 循环n-1轮，每轮对m条边进行一次松弛操作

# 定理：
# 在一个含有n个顶点的图中，任意两点之间的最短路径最多包含n-1条边
# 最短路径肯定是一个不包含回路的简单路径（回路包括正权回路与负权回路）
# 1. 如果最短路径中包含正权回路，则去掉这个回路，一定可以得到更短的路径
# 2. 如果最短路径中包含负权回路，则每多走一次这个回路，路径更短，则不存在最短路径
# 因此最短路径肯定是一个不包含回路的简单路径，即最多包含n-1条边，所以进行n-1次松弛即可


G = {'a':{'a':0, 'b':-3, 'e':5},
    'b':{'b':0, 'c':2},
      'c':{'c':0, 'd':3},
      'd':{'d':0, 'e':2},
      'e':{'e':0}}


def getEdges(G):
     """ 输入图G，返回其边与端点的列表 """
     v1 = []     # 出发点
     v2 = []     # 对应的相邻到达点
     w  = []     # 顶点v1到顶点v2的边的权值
     for i in G:
         for j in G[i]:
             if G[i][j] != 0:
                 w.append(G[i][j])
                 v1.append(i)
                 v2.append(j)
     return v1,v2,w


class CycleError(Exception):
     pass


def Bellman_Ford(G, v0, INF=999):
     v1,v2,w = getEdges(G)

     # 初始化源点与所有点之间的最短距离
     dis = dict((k,INF) for k in G.keys())
     path=dict((k,'') for k in G.keys())
     dis[v0] = 0


     # 核心算法
     for k in range(len(G)-1):   # 循环 n-1轮
         check = 0           # 用于标记本轮松弛中dis是否发生更新
         for i in range(len(w)):     # 对每条边进行一次松弛操作
             if dis[v1[i]] + w[i] < dis[v2[i]]:
                 dis[v2[i]] = dis[v1[i]] + w[i]
                 path[v2[i]]=v1[i]
                 check = 1
         if check == 0: break

     # 检测负权回路
     # 如果在 n-1 次松弛之后，最短路径依然发生变化，则该图必然存在负权回路
     flag = 0
     for i in range(len(w)):             # 对每条边再尝试进行一次松弛操作
         if dis[v1[i]] + w[i] < dis[v2[i]]:
             flag = 1
             break
     if flag == 1:
 #         raise CycleError()
         return False
     return dis,path

if __name__=="__main__":
    v0 = 'a'
    graph = {
        'a': {'b': -1, 'c': 4},
        'b': {'c': 2, 'd': 3, 'e': 2},
        'c': {},
        'd': {'b': 3, 'c': 5},
        'e': {'d': -3}
    }

    dis,path = Bellman_Ford(graph, v0)
    print (dis)
    print(path)

   