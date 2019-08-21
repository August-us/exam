graph = {
    'a': ['b', 'c'],
    'b': ['a', 'c', 'd'],
    'c': ['a', 'b', 'd', 'e'],
    'd': ['b', 'c', 'e', 'f'],
    'e': ['c', 'd'],
    'f': ['d']
}


def BFS(graph, s):
    queue = []
    queue.append(s)
    seen = set()
    seen.add(s)
    while len(queue) > 0:
        vertex = queue.pop(0)
        nodes = graph[vertex]
        for node in nodes:
            if node not in seen:
                queue.append(node)
                seen.add(node)
        print(vertex)


BFS(graph, 'a')


def DFS(graph, s):
    stack = []
    stack.append(s)
    seen = set()
    seen.add(s)
    while len(stack) > 0:
        vertex = stack.pop()
        nodes = graph[vertex]
        for node in nodes:
            if node not in seen:
                stack.append(node)
                seen.add(node)
        print(vertex)


DFS(graph, 'a')


def DFS1(graph, s, queue=[]):
    queue.append(s)
    for i in graph[s]:
        if i not in queue:
            DFS1(graph, i, queue)
    return queue


print(DFS1(graph, 'a'))

from collections import defaultdict
from heapq import *


def Prim(vertexs, edges, start_node):
    adjacent_vertex = defaultdict(list)
    for v1, v2, length in edges:
        adjacent_vertex[v1].append((length, v1, v2))
        adjacent_vertex[v2].append((length, v2, v1))

    mst = []
    closed = set(start_node)

    adjacent_vertexs_edges = adjacent_vertex[start_node]
    heapify(adjacent_vertexs_edges)

    while adjacent_vertexs_edges:
        w, v1, v2 = heappop(adjacent_vertexs_edges)
        if v2 not in closed:
            closed.add(v2)
            mst.append((v1, v2, w))

            for next_vertex in adjacent_vertex[v2]:
                if next_vertex[2] not in closed:
                    heappush(adjacent_vertexs_edges, next_vertex)

    return mst


vertexs = list("ABCDEFG")
edges = [("A", "B", 7), ("A", "D", 5),
         ("B", "C", 8), ("B", "D", 9),
         ("B", "E", 7), ("C", "E", 5),
         ("D", "E", 15), ("D", "F", 6),
         ("E", "F", 8), ("E", "G", 9),
         ("F", "G", 11)]

print('prim:', Prim(vertexs, edges, 'A'))

# ****************************************************


node = dict()
rank = dict()


def make_set(point):
    node[point] = point
    rank[point] = 0


def find(point):
    if node[point] != point:
        node[point] = find(node[point])
    return node[point]


def merge(point1, point2):
    root1 = find(point1)
    root2 = find(point2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            node[root2] = root1
        else:
            node[root1] = root2
            if rank[root1] == rank[root2]: rank[root2] += 1


def Kruskal(graph):
    for vertice in graph['vertices']:
        make_set(vertice)

    mst = set()

    edges = list(graph['edges'])
    edges.sort()
    for edge in edges:
        weight, v1, v2 = edge
        if find(v1) != find(v2):
            merge(v1, v2)
            mst.add(edge)
    return mst

graph = {
    'vertices': ['A', 'B', 'C', 'D'],
    'edges': set([
        (1, 'A', 'B'),
        (5, 'A', 'C'),
        (3, 'A', 'D'),
        (4, 'B', 'C'),
        (2, 'B', 'D'),
        (1, 'C', 'D'),
        ])
    }

print(Kruskal(graph))