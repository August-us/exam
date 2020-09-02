# 这个题目的最大不同在于需要使用三个指针，这样就会让边界处理变得更加麻烦
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        if self.next:
            return str(self.val)+' '+str(self.next)
        else:
            return str(self.val)

pHead=ListNode(0)
p=pHead
# for i in [1,2,3,3,4,4,5]:
for i in [1,1,1,1,1,1,1]:
    p.next=ListNode(i)
    p=p.next


class Solution:
    def deleteDuplication(self, pHead):
        if not pHead:
            return None

        p=pHead
        pPreNode=None
        while p:
            pNext=p.next
            needDelete=False
            if pNext and pNext.val==p.val:
                needDelete=True
            if not needDelete:
                pPreNode=p
                p=p.next
            else:
                value=p.val
                while p and p.val==value:
                    pNext=p.next
                    p=pNext
                if not pPreNode:
                    pHead=pNext
                else:
                    pPreNode.next=pNext
                p=pNext
        return pHead

class Solution1:
    def deleteDuplication(self, pHead):
        # 自己创建一个节点，保证prePNode始终存在
        res=ListNode('')
        res.next=pHead
        p=pHead
        pPreNode=res
        while p and p.next:
            value=p.next.val
            if p.val==value:
                while p and p.val==value:
                    p =p.next
            else:
                pPreNode=p
                p=p.next
            pPreNode.next = p
        return res.next

print(Solution1().deleteDuplication(pHead.next))

