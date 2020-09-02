from TestCase import ListNode, TreeNode

'''
给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

示例:

给定的有序链表： [-10, -3, 0, 5, 9],

一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /

'''
class Solution:
    def findSize(self, head):
        ptr = head
        c = 0
        while ptr:
            ptr = ptr.next
            c += 1
        return c

    def sortedListToBST(self, head: ListNode) -> TreeNode:
        '''
        根据中序遍历的顺序去构造二叉树，正好中序遍历的顺序就是链表的顺序，中序遍历是递归的
        '''
        size = self.findSize(head)

        def convert(l, r):
            nonlocal head
            if l > r:
                return None
            mid = (l + r) // 2

            # 中序遍历左子树
            left = convert(l, mid - 1)

            # 构造左子树之后构造当前节点
            node = TreeNode(head.val)
            node.left = left

            head = head.next

            node.right = convert(mid + 1, r)
            return node
        return convert(0, size - 1)

head=ListNode.create_list( [-10, -3, 0, 5, 9])
Solution().sortedListToBST(head).printTree()