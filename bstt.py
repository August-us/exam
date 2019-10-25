class TNode:
    def __init__(self, key, left, right, parent):
        self.key = key
        self.lchild = left
        self.rchild = right
        self.parent = parent


class PTNode:
    def __init__(self, TNode):
        self.TNode = TNode


def InsertNode(BST, key,res):
    Pparent = PTNode(BST)
    parent = Pparent.TNode
    Node = TNode(key, None, None, None)
    if None == parent or None == parent.key:
        return True
    if key > parent.key:
        if parent.rchild:
            InsertNode(parent.rchild,key,res)
        else:
            parent.rchild = Node
            Node.parent = parent
            res.append(parent.key)

    else:
        if parent.lchild:
            InsertNode(parent.lchild,key,res)
        else:
            parent.lchild = Node
            Node.parent = parent
            res.append(parent.key)

    return True

if __name__ == '__main__':
    n=int(input())
    A=[int(i) for i in input().split(' ')]
    BST = TNode(A[0], None, None, None)
    Pparent = PTNode(BST)
    Psearch = PTNode(BST)
    res=[]
    for i in  A[1:]:
        InsertNode(BST, i,res)
    print(' '.join(map(str,res)))
'''
5
8 9 2 3 7
'''