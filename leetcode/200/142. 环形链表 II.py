from TestCase import ListNode

'''
给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
说明：不允许修改给定的链表。

示例 1：

输入：head = [3,2,0,-4], pos = 1
输出：2
解释：链表中有一个环，其尾部连接到第二个节点。


示例 2：

输入：head = [1,2], pos = 0
输出：1
解释：链表中有一个环，其尾部连接到第一个节点。


示例 3：

输入：head = [1], pos = -1
输出：no cycle
解释：链表中没有环。
'''
class Solution:
    def detectCycle_withcount(self, head: ListNode) -> ListNode:
        p=q=head
        k = 0
        while q and q.next:
            p=p.next
            q=q.next.next
            k += 1
            if p==q:
                p = q =head
                while k:
                    p = p.next
                    k-=1
                while p!=q:
                    p = p.next
                    q = q.next
                    k+=1
                return p

    def detectCycle(self, head: ListNode) -> ListNode:
        # 相遇节点，然后让p回头投节点，p从头节点开始，q从相遇节点开始，下次相遇一定是环的起始位置
        # fast = nc, s = 0, fast = nc+a s = a 显然当a是环的起始节点，fast 和slow相遇
        p=q=head
        k = 0
        while q and q.next:
            p=p.next
            q=q.next.next
            if p==q:
                p =head
                while p!=q:
                    p = p.next
                    q = q.next
                return p
