from typing import List
from TestCase import TreeNode

'''
给定一个二叉树，返回它的 后序 遍历。

示例:

输入: [1,null,2,3]  
   1
    \
     2
    /
   3 
输出: [3,2,1]
'''

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res =[]
        stack = [root] if root else []
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)

        return res[::-1]

    def postorderTraversal_flag(self, root: TreeNode) -> List[int]:
        # 通过标记记录是否访问完孩子节点
        res = []
        stack = [[root, 0]] if root else []
        while stack:
            if not stack[-1][1]:
                cur = stack[-1]
                if cur[0].right:
                    stack.append([cur[0].right, 0])
                if cur[0].left:
                    stack.append([cur[0].left, 0])
                cur[1] = 1
            else:
                cur = stack.pop()
                res.append(cur[0].val)
        return res

null = '$'
root = TreeNode.deserialize( [1,null,2,3])
for i in Solution().postorderTraversal(root):print(i, end=' ')

