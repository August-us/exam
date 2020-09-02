from TestCase import ListNode

'''
给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL
解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL
示例 2:

输入: 0->1->2->NULL, k = 4
输出: 2->0->1->NULL
解释:
向右旋转 1 步: 2->0->1->NULL
向右旋转 2 步: 1->2->0->NULL
向右旋转 3 步: 0->1->2->NULL
向右旋转 4 步: 2->0->1->NULL
'''
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        p=head
        i=1
        while i<=k:
            if not p.next:
                k=k%i
                i=1
                p=head
            else:
                p=p.next
                i+=1
        q=head
        if k == 0:
            return head
        while p.next:
            p=p.next
            q=q.next
        newHead=q.next
        q.next=None
        p.next=head
        return newHead
head=ListNode.create_list([1])
print(Solution().rotateRight(head,1))