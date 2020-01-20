# -*- coding:utf-8 -*-

# 输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __iter__(self):
        p=self
        while p:
            yield p.val
            p=p.right
class Solution:
    def Convert(self, pRootOfTree):
        if not pRootOfTree:
            return
        self.pre=None
        self.inOrder(pRootOfTree)
        while pRootOfTree.left:
            pRootOfTree=pRootOfTree.left
        return pRootOfTree

    def inOrder(self,root):
        if root:
            self.inOrder(root.left)
            root.left=self.pre
            if self.pre:
                self.pre.right=root
            self.pre=root
            self.inOrder(root.right)

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

root=bulidTree([5,2,10,1,3,9,20])
print(list(Solution().Convert(root)))