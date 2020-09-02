from typing import List

from TestCase import TreeNode
'''
给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树。

示例:

输入: 3
输出:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
解释:
以上的输出对应以下 5 种不同结构的二叉搜索树：

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

'''

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def generateTrees(start,end):
            if end==start+1:return [TreeNode(end)]
            elif end==start:return [None]
            res=[]
            for i in range(start,end):
                left=generateTrees(start,i)
                right=generateTrees(i+1,end)
                for l in left:
                    for  r in right:
                        curNode=TreeNode(i+1)
                        curNode.left=l
                        curNode.right=r
                        res.append(curNode)
            return res
        return generateTrees(0,n) if n else []

print(Solution().generateTrees(3))




