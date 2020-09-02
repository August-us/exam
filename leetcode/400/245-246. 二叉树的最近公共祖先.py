from TestCase import TreeNode


class Solution:
    '''
    给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。

    百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

    例如，给定如下二叉搜索树:  root = [6,2,8,0,4,7,9,null,null,3,5]
    示例 1:

    输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
    输出: 6 
    解释: 节点 2 和节点 8 的最近公共祖先是 6。
    示例 2:

    输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
    输出: 2
    解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。
     

    说明:

    所有节点的值都是唯一的。
    p、q 为不同节点且均存在于给定的二叉搜索树中。
    '''''

    def lowestCommonAncestor_serachtree(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> TreeNode:
        trace, res = set(), root
        proot = root
        while proot.val != p.val:
            trace.add(proot)
            if proot.val < p.val:
                proot = proot.right
            else:
                proot = proot.left
        trace.add(proot)
        while True:
            if root in trace:
                res = root
            if root.val == q.val:
                break
            if root.val < q.val:
                root = root.right
            else:
                root = root.left
        return res

    def lowestCommonAncestor_serachTree(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        minNode, maxNode = min(p.val, q.val), max(p.val, q.val)
        while root:
            if minNode > root.val:
                root = root.right
            elif maxNode < root.val:
                root = root.left
            else:
                return root

    '''
    不要求是二叉搜索树的情况
    '''

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ppath, qpath = None, None

        def dfs(root, path):
            nonlocal ppath, qpath
            if not root or (ppath and qpath):
                return
            path.append(root)
            if root.val == q.val:
                qpath = path.copy()
            if root.val == p.val:
                ppath = path.copy()
            dfs(root.left, path)
            dfs(root.right, path)
            path.pop()

        dfs(root, [])
        res = root
        for i, j in zip(qpath, ppath):
            if i == j:
                res = i
        return res


null = '$'
root = TreeNode.createTree([3, 5, 1, 6, 2, 0, 8, null, null, 7, 4])

root.printTree()
print(Solution().lowestCommonAncestor(root, TreeNode(5), TreeNode(4)))