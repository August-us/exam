class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def printNode(self,d=0):
        print('  ' * d, end='')
        print(self.val)
        if self.left:
            print('  '*d,end='')
            self.left.printNode(d+1)
        if self.right:
            print('  '*d,end='')
            self.right.printNode( d + 1)
    def __str__(self):
        self.printNode()
        return ''



class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        if not pre:
            return None
        root=TreeNode(pre[0])
        ind=tin.index(pre[0])
        root.left=self.reConstructBinaryTree(pre[1:ind+1],tin[:ind])
        root.right=self.reConstructBinaryTree(pre[ind+1:],tin[ind+1:])

        return root
print(Solution().reConstructBinaryTree([1,2,4,7,3,5,6,8],[4,7,2,1,5,3,8,6]))
