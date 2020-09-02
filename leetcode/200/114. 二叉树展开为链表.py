from TestCase import TreeNode

'''
给定一个二叉树，原地将它展开为链表。

例如，给定二叉树

    1
   / \
  2   5
 / \   \
3   4   6
将其展开为：

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
'''

class Solution:
    def flatten_withlist(self, root: TreeNode) -> None:
        # 通过list保存顺序，然后进行修改
        if not root: return
        l = []

        def visit(root, l):
            l.append(root)
            if root.left:
                visit(root.left, l)
            if root.right:
                visit(root.right, l)

        visit(root, l)
        l.append(None)
        for i in range(len(l) - 1):
            l[i].right = l[i + 1]
            l[i].left = None

    def flatten_recur(self, root: TreeNode) -> None:
        # 递归版本，先初始化左子树，然后找到左子树链表的尾节点，然后进行拼接
        if not root: return
        self.flatten(root.right)
        right = root.right
        self.flatten(root.left)
        root.right, root.left = root.left, None
        while root.right:
            root = root.right
        root.right = right

    def flatten(self, root: TreeNode) -> None:
        # 保存一个pre的元素，只需要对这个元素进行修改即可，是以上两个版本的改进
        if not root: return
        self.pre = root
        def visit(root):
            self.pre.right=root
            self.pre.left=None
            self.pre=root
            right=root.right if root.right else None
            if root.left:
                visit(root.left)
            if right:
                visit(right)

        right = root.right if root.right else None
        if root.left:
            visit(root.left)
        if right:
            visit(right)


null='$'
root=TreeNode.createTree([1,2,5,3,4,null,6])
Solution().flatten(root)
root.printTree()
