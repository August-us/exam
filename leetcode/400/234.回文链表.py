from TestCase import ListNode

'''
请判断一个链表是否为回文链表。
示例 1:
输入: 1->2
输出: false
示例 2:
输入: 1->2->2->1
输出: true
进阶： 你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
'''
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # 空间复杂度O(n)
        p = q = head
        stack = []
        while q and q.next:
            stack.append(p)
            p = p.next
            q = q.next.next
        if q:
            p = p.next
        for i in reversed(stack):
            if not p  or i.val!=p.val:
                return False
            p = p.next
        return True
    def isPalindrome(self, head: ListNode) -> bool:
        # 空间复杂度O(1)
        p = q = head
        while q and q.next:
            pre = p
            p = p.next
            q = q.next.next
        if q:
            pre = p
            p = p.next
            pre.next = None
        def reverse(p):
            newHead = ListNode('')
            while p:
                q = p
                p = p.next
                q.next = newHead.next
                newHead.next = q
            return newHead.next
        p = reverse(p)
        q = head
        while q.next:
            if q.val != p.val:
                return False
            q = q.next
            p = p.next
        return True




head = ListNode.create_list([1,2, 1,2])
print(Solution().isPalindrome(head))