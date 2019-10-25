# BST.py
_Debug = False


# +++++++++++++++++++++struct realized by class+++++++++++++++++++++#
class TNode:
    def __init__(self, key, left, right, parent):
        self.key = key
        self.lchild = left
        self.rchild = right
        self.parent = parent


class PTNode:
    def __init__(self, TNode):
        self.TNode = TNode


# +++++++++++++++++++++++++search operation+++++++++++++++++++++++++#
def SearchBST(BST, key, search, parent):
    if None == BST or None == BST.key:
        return False
    if key == BST.key:
        parent.TNode = BST.parent
        search.TNode = BST
        return True
    elif key < BST.key:
        parent.TNode = BST
        return SearchBST(BST.lchild, key, search, parent)
    else:
        parent.TNode = BST
        return SearchBST(BST.rchild, key, search, parent)
    return False


# +++++++++++++++++++++++++Insert operation+++++++++++++++++++++++++#
def InsertNode(BST, key, search):
    Pparent = PTNode(BST)
    Psearch = PTNode(BST)
    if _Debug == True:
        import pdb
        pdb.set_trace()
    if SearchBST(BST, key, Psearch, Pparent):
        return False
    parent = Pparent.TNode
    search = Psearch.TNode
    Node = TNode(key, None, None, None)
    if None == parent or None == parent.key:
        BST = Node
        return True
    if key > parent.key:
        parent.rchild = Node
    else:
        parent.lchild = Node
    Node.parent = parent
    search = Node
    return True


# +++++++++++++++++++++++++Delete operation+++++++++++++++++++++++++#
def DeleteNode(BST, key):
    Pparent = PTNode(BST)
    Psearch = PTNode(BST)
    if False == SearchBST(BST, key, Psearch, Pparent):
        return False
    parent = Pparent.TNode
    search = Psearch.TNode
    if None != search.lchild and None != search.rchild:
        tmp = search
        while (None != tmp.lchild):
            tmp = tmp.lchild
        tmp.lchild = search.lchild
        if None != parent and search == parent.lchild:

            parent.lchild = search.rchild
            search.rchild.parent = parent
        elif None != parent and search == parent.rchild:
            parent.rchild = search.rchild
            search.rchild.parent = parent

    elif None != search.lchild:
        if None != parent and search == parent.lchild:
            parent.lchild = search.lchild
            search.lchild.parent = parent
        elif None != parent and search == parent.rchild:
            parent.rchild = search.lchild
            search.lchild.parent = parent
    elif None != search.rchild:
        if None != parent and search == parent.lchild:
            parent.lchild = search.rchild
            search.rchild.parent = parent
        elif None != parent and search == parent.rchild:
            parent.rchild = search.rchild
            search.rchild.parent = parent
    else:
        parent.lchild = None
        parent.rchild = None
    del search
    search = None
    return True


# +++++++++++++++++++++++++Release operation+++++++++++++++++++++++++#
def DeleteBST(BST):
    if None != BST:
        if None == BST.lchild and None == BST.rchild:
            tmp = BST.parent
            if tmp != None and tmp.lchild == BST:
                tmp.lchild = None
            elif tmp != None and tmp.rchild == BST:
                tmp.rhicld = None
            del BST
            BST = None
            return
        DeleteBST(BST.lchild)
        DeleteBST(BST.rchild)


# +++++++++++++++++++++++++Print  operation+++++++++++++++++++++++++#
def PrintBST(BST):
    if None == BST:
        return
    print(BST.key)
    PrintBST(BST.lchild)
    PrintBST(BST.rchild)


# ++++++++++++++++++++++++++Test operation++++++++++++++++++++++++++#
if __name__ == '__main__':
    BST = TNode(0, None, None, None)
    Pparent = PTNode(BST)
    Psearch = PTNode(BST)
    for i in range(1, 4):
        if False == InsertNode(BST, i, Psearch.TNode):
            print
            'Insert Number %d Failed.' % (i)
    print
    'print BST:'
    PrintBST(BST)
    if True == SearchBST(BST, 1, Psearch, Pparent):
        print
        'Find 1 in BST Sucess.'
    if True == DeleteNode(BST, 1):
        print
        'Delete 1 Success.'
    if False == SearchBST(BST, 1, Psearch, Pparent):
        print
        'Find 1 in BST Failed.'

    DeleteBST(BST)
    print
    'Done'