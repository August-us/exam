# 对于一个具有树特征的无向图，我们可选择任何一个节点作为根。图因此可以成为树，在所有可能的树中，具有最小高度的树被称为最小高度树。给出这样的一个图，写出一个函
# 数找到所有的最小高度树并返回他们的根节点。
#
#  格式
#
#  该图包含 n 个节点，标记为 0 到 n - 1。给定数字 n 和一个无向边 edges 列表（每一个边都是一对标签）。
#
#  你可以假设没有重复的边会出现在 edges 中。由于所有的边都是无向边， [0, 1]和 [1, 0] 是相同的，因此不会同时出现在 edges 里。
#
#  示例 1:
#
#  输入: n = 4, edges = [[1, 0], [1, 2], [1, 3]]
#
#         0
#         |
#         1
#        / \
#       2   3
#
# 输出: [1]
#
#
#  示例 2:
#
#  输入: n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
#
#      0  1  2
#       \ | /
#         3
#         |
#         4
#         |
#         5
#
# 输出: [3, 4]
#
#  说明:
#
#
#  根据树的定义，树是一个无向图，其中任何两个顶点只通过一条路径连接。 换句话说，一个任何没有简单环路的连通图都是一棵树。
#  树的高度是指根节点和叶子节点之间最长向下路径上边的数量。
#
#  Related Topics 广度优先搜索 图
#  👍 176 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        degree = [0 for i in range(n)]
        visited = {i for i in range(n)}

        cur = 0
        zero_degree = [set(), set()]
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)

        for i,j in graph.items():
            degree[i] = len(j)
            if degree[i]==1:
                zero_degree[cur].add(i)
        while zero_degree[cur]:
            if len(visited) <= 2:
                return list(zero_degree[cur])
            for i in zero_degree[cur]:
                visited.remove(i)
                for j in graph[i]:
                    degree[j] -= 1
                    if degree[j]==1:
                        zero_degree[1^cur].add(j)
            zero_degree[cur].clear()
            cur ^= 1
        return list(range(n))

class Solution_force:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n<=1:return [0]
        def floyd(distance):
            lengthD = len(distance)  # 邻接矩阵大小
            path = [[j for i in range(lengthD)] for j in range(lengthD)]
            for k in range(lengthD):
                for i in range(lengthD):
                    for j in range(lengthD):
                        if (distance[i][j] > distance[i][k] + distance[k] [j]):  # 两个顶点直接较小的间接路径替换较大的直接路径
                            distance[i][j] = distance[i][k] + distance[k][ j]  # 记录新路径的前驱
                            path[i][j] = k
            return distance
        matrix = [[n if i!=j else 0 for j in range(n)] for i in range(n)]

        for s,e in edges:
            matrix[s][e] = 1
            matrix[e][s] = 1
        distance = floyd(matrix)
        print(distance)
        res, minNode = [], float('inf')
        for i, arr in enumerate(distance):
            if minNode > max(arr):
                res = [i]
                minNode = max(arr)
            elif minNode== max(arr):
                res.append(i)
        return res


print(Solution().findMinHeightTrees(3 ,[[0,1],[0,2]]))
print(Solution().findMinHeightTrees(n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]))
print(Solution_force().findMinHeightTrees(4
,[[1,0],[1,2],[1,3]]))
print(Solution_force().findMinHeightTrees(n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]))
