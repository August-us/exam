from pylab import array

M=INF = float('inf')                        #代表无穷大
D = array([[0,10,INF,INF,INF,11,INF,INF,INF],#邻接矩阵
        [10,0,18,INF,INF,INF,16,INF,12],
        [INF,18,0,22,INF,INF,INF,INF,8],
        [INF,INF,22,0,20,INF,INF,16,21],
        [INF,INF,INF,20,0,26,INF,7,INF],
        [11,INF,INF,INF,26,0,17,INF,INF],
        [INF,16,INF,24,INF,17,0,19,INF],
        [INF,INF,INF,16,7,INF,19,0,INF],
        [INF,12,8,21,INF,INF,INF,INF,0]])
def floyd(D):
    lengthD = len(D)                    #邻接矩阵大小
    distance = D.copy()
    distance = array(distance)
    path=array([[j for i in range(lengthD)] for j in range(lengthD)])

    for k in range(lengthD):
        for i in range(lengthD):
            for j in range(lengthD):
                if(distance[i,j] > distance[i,k]+distance[k,j]):         #两个顶点直接较小的间接路径替换较大的直接路径
                    distance[i, j] = distance[i, k] + distance[k, j]            #记录新路径的前驱
                    path[i,j]=k
    print(distance)
    print(path)

if __name__ =="__main__":
    G = [
        [0, 30, 15, M, M, M],
        [5, 0, M, M, 20, 30],
        [M, 10, 0, M, M, 15],
        [M, M, M, 0, M, M],
        [M, M, M, 10, 0, M],
        [M, M, M, 30, 10, 0]
    ]

    floyd(array(G))