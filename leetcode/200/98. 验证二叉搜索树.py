from TestCase import TreeNode

'''
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
示例 1:

输入:
    2
   / \
  1   3
输出: true
示例 2:

输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。
'''
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        inroder=self.inorderTraversal(root)
        for i in range(1,len(inroder)):
            if inroder[i]<inroder[i-1]:
                return False
        return True
    def inorderTraversal(self,root):
        stack = []
        res = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            p = stack.pop()
            res.append(p.val)
            root = p.right
        return res

    def isValidBST_recursive(self, root: TreeNode,lower= float('-inf'),upper= float('inf')) -> bool:
        if not root:return True
        if root.val<=lower or root.val>=upper:return False
        return self.isValidBST(root.left,lower,root.val) and self.isValidBST(root.right,root.val,upper)

    def recoverTree(self, root: TreeNode) -> None:
        """
        二叉搜索树中的两个节点被错误地交换。请在不改变其结构的情况下，恢复这棵树。
        想到中序遍历，然后把违反顺序的两个节点交换，第一个错误节点比后面的节点大，第二个错误节点比前面的节点小，两个节点可能紧挨，比前面节点小的节点可能有两个
        该算法可以写成非递归的
        # 这个题还有一种思路就是，在遍历的时候，边遍历，边对树进行线索化，然后只需要记录一个节点，就可以完成遍历，但是会修改树
        """
        self.disorder1=None
        self.disorder2=None
        self.pre=TreeNode(float('-inf'))
        try:self.recover(root)
        except:pass
        self.disorder1.val,self.disorder2.val=self.disorder2.val,self.disorder1.val

    def recover(self, root: TreeNode):
        if root.left:self.recover(root.left)
        if root.val < self.pre.val:
            self.disorder2 = root
            if self.disorder1: # 这里主要是为了防止两个需要交换的结点紧邻，此时root.val < self.pre.val可能只会满足一次
                raise Exception
            self.disorder1=self.pre
        self.pre=root
        if root.right:self.recover(root.right)
