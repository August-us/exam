from TestCase import TreeNode
'''
给定一个二叉树

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

初始状态下，所有 next 指针都被设置为 NULL。

 

进阶：

你只能使用常量级额外空间。
使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。
 

示例：



输入：root = [1,2,3,4,5,null,7]
输出：[1,#,2,3,#,4,5,7,#]
解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。
 

提示：

树中的节点数小于 6000
-100 <= node.val <= 100
'''

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        node=root
        while node:
            leftmost = None
            pre = None
            while node:
                if leftmost:
                    if node.left:
                        pre.next = node.left
                        pre = node.left
                    if node.right:
                        pre.next = node.right
                        pre = node.right

                else:
                    if node.left:
                        leftmost = node.left
                        pre = leftmost
                        continue
                    if node.right:
                        leftmost = node.right
                        pre = leftmost
                node = node.next if node != node.next else None
            node = leftmost
        return root

    def connect(self, root: 'Node') -> 'Node':
            node = root
            while node:
                leftmost = None
                pre = None
                while node:
                    if leftmost:
                        if node.left:
                            pre.next = node.left if pre != node.left else None
                            pre = node.left
                        if node.right:
                            pre.next = node.right if pre != node.right else None
                            pre = node.right
                    else:
                        if node.left:
                            leftmost = node.left
                            pre = leftmost
                            continue
                        if node.right:
                            leftmost = node.right
                            pre = leftmost
                    node = node.next
                node = leftmost
            return root
null='$'
root=TreeNode.createTree([1,2])
root.printTree()
root=Solution().connect(root)
root.printTree()