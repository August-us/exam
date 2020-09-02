from typing import List

res=[]
class Node:
    '''
    图的节点
    '''
    matrix = None

    def __init__(self, val = 0, neighbors = [], matrix=None):
        self.val = val
        self.neighbors = neighbors
        self.matrix = matrix

    @classmethod
    def createGraph(cls,list:List[List[int]]) -> 'Node':
        matrix = [[0]*len(list) for i in range(len(list))]
        nodes = [Node(i+1,matrix=matrix) for i in range(len(list))]

        for i,n in enumerate(list):
            nodes[i].neighbors = [nodes[i-1] for i in n]
            matrix[i][i] = 1
            for _ in n:matrix[i][_-1] = 1
        return nodes[0]

    def __str__(self):
        return str(self.val)



class stack(list):
    def order(self):
        for i in ["PSH3", "MIN", "PSH4", "MIN", "PSH2", "MIN", "PSH3", "MIN", "POP", "MIN", "POP", "MIN", "POP", "MIN",
                  "PSH0", "MIN"]:
            if i[0:3] == 'PSH':
                a.push(int(i[3]))
            elif i == 'MIN':
                res.append(a.min())
            elif i == 'POP':
                a.pop()
            print(a.a)
            print(a.orderA)
a=stack()

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    @classmethod
    def create_list(self,l):
        p=head=ListNode('')
        for i in l:
            p.next=ListNode(i)
            p=p.next
        return head.next

    def __str__(self):
        if self.next:
            return str(self.val)+' '+str(self.next)
        else:
            return str(self.val)

    def __lt__(self, other):
        return self.val<other.val

    def __gt__(self, other):
        return self.val>other.val

null = '$'
class TreeNode:
    def __init__(self, x,left=None,right=None):
        self.val = x
        self.left = left
        self.right = right
        # self.next = None

    def __str__(self):
        return str(self.val)

    def serialize(self):
        serializer=str(self)
        if self.left:
            serializer+=','+self.left.serialize()
        else:
            serializer+=",$"
        if self.right:
            serializer+=','+self.right.serialize()
        else:
            serializer+=",$"
        return serializer
    @classmethod
    def deserialize(self,serializer): # 根据中序序列构建树
        if isinstance(serializer,str):
            serializer=serializer.split(',')
        if not serializer:return
        value=serializer.pop(0)
        if not value or value=='$':
            return
        root=TreeNode(int(value))
        root.left=TreeNode.deserialize(serializer)
        root.right=TreeNode.deserialize(serializer)
        return root

    def printTree(self, d=0):
        print('  ' * d, self.val)
        if self.left:
            self.left.printTree(d + 1)
        if self.right:
            self.right.printTree(d + 1)

    @classmethod
    def createTree(self,data):
        if isinstance(data,str):
            data=data.split(',')
        k = cur = 0
        root=TreeNode(int(data[0]))
        data[0]=root
        couldParent = [root]

        for i in range(1,len(data)):
            try:
                node=TreeNode(int(data[i]))
            except:node=None
            if node:
                couldParent.append(node)
            if i%2:
                couldParent[cur].left=node
            else:
                couldParent[cur].right = node
                cur +=1


            data[i]=node
        return root

    def Level(self):
        left=[self]
        right=[]
        res=[]
        while left:
            def level(x):
                if x.left:
                    right.append(x.left)
                if x.right:
                    right.append(x.right)
                return x.val
            res.append(list(map(level, left)))
            left,right=right,[]
        return res

    def inorderTraversal(self):
        stack=[]
        res=[]
        root=self
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            p=stack.pop()
            res.append(p.val)
            root=p.right
        return res

class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

    def __iter__(self):
        p=self
        while p:
            yield p.label
            p=p.next


    def __str__(self):
        if self.next is None:
            return str(self.label)
        else:
            return str(self.label)+','+str(self.next)

alpha='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

