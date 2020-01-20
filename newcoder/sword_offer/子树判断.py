# -*- coding:utf-8 -*-

# 输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
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


class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if not pRoot1 or not pRoot2:
            return False
        if pRoot1.val==pRoot2.val:
            if self.compare(pRoot1,pRoot2):
                return True
        return self.HasSubtree(pRoot1.left,pRoot2) or self.HasSubtree(pRoot1.right,pRoot2)

    def compare(self,pRoot1, pRoot2):
        if not pRoot2:
            return True
        if  not pRoot1 or pRoot1.val != pRoot2.val:
            return False
        return self.compare(pRoot1.left,pRoot2.left) and self.compare(pRoot1.right,pRoot2.right)

a=bulidTree([8,-1,8,-1,9,-1,2,-1,5])
b=bulidTree([8,-1,9,3,2])
printTree(a)
printTree(b)
print(Solution().HasSubtree(a,b))
