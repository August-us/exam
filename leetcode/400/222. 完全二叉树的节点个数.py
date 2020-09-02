import random

from TestCase import TreeNode

'''
给出一个完全二叉树，求出该树的节点个数。

说明：

完全二叉树的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h 层，则该层包含 1~ 2h 个节点。

示例:

输入: 
    1
   / \
  2   3
 / \  /
4  5 6
'''
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        queue = [root] if root else []
        res = 0
        while queue:
            root = queue.pop(0)
            res += 1
            if not root.left:
                return res + len(queue)
            queue.append(root.left)
            if not root.right:
                return res + len(queue)
            queue.append(root.right)
    def countNodes(self, root: TreeNode) -> int:
        # 二分法
        if not root:return 0
        start, end = 1, 3
        p = root
        while p.right:
            start, end = end, end*2+1
            p = p.right

        def isExists(mid):
            p = root
            stack = []
            while mid > 1:
                stack.append(mid&1)
                mid >>=1
            for i in reversed(stack):
                if i:
                    p = p.right
                else:
                    p = p.left
            return not p is None



        while start<end-1:
            mid = (start+end)>>1
            if isExists(mid):
                start = mid
            else:
                end = mid
        return start


n = random.randint(0, 100)
print(n)
root = TreeNode.createTree(list(range(1,n+1)))

print(Solution().countNodes(root))




