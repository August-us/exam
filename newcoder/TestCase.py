res=[]
class stack(list):
    pass
a=stack()
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

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)

def printTree(root,d=0):
    if root.val !=-1:
        print('  '*d,end='')
        print(root.val)
        if root.left:
            printTree(root.left,d+1)
        if root.right:
            printTree(root.right,d+1)

def bulidTree(a):
    root=TreeNode(a[0])
    t=[]
    t.append(root)
    for i in range(1,len(a),2):
        cur=t.pop(0)
        cur.left=TreeNode(a[i])
        cur.right=TreeNode(a[i+1])
        t.extend([cur.left,cur.right])
    return root


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

a='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
