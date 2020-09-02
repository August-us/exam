from collections import defaultdict


def union_find(edges):
    node_father = {}
    def getroot(node):
        if node not in node_father:
            node_father[node] = node
        elif node_father[node_father[node]] != node_father[node]:
            node_father[node] = getroot(node_father[node])
        return node_father[node]

    for edge in edges:
        if edge[0] not in node_father:
            node_father[edge[0]] = getroot(edge[1])
        elif edge[1] not in node_father :
            node_father[edge[1]] = getroot(edge[0])
        else:
            node_father[getroot(edge[0])] = getroot(edge[1])
    return node_father