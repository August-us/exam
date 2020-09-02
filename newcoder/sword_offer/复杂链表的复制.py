import random


class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

    def __iter__(self):
        p=self
        while p:
            yield str(p)
            p=p.next


    def __str__(self):
        if self.random:
            return "%d->%d.(%d:%d)"%(self.label,self.random.label,id(self.random),id(self.random))
        else:
            return "%d->None(%d:)"%(self.label,id(self.random))


class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        if not pHead:
            return
        current=pHead
        while current:
            # 第一趟扫描，在旧节点的后面插入新节点
            newNode=RandomListNode(current.label)
            newNode.next=current.next
            current.next=newNode
            current=newNode.next
        current=pHead
        while current:
            # 第二趟扫描，修改random指针域
            newNode=current.next
            if current.random:
                newNode.random=current.random.next
            current=newNode.next
        current=pHead
        newNode=newHead=current.next
        current.next=newNode.next
        current=current.next
        # while current.next: # current节点在每次前进一个节点
        #     # 第三趟扫描，开始分节点
        #     newNode=current.next
        #     current.next=newNode.next
        #     current=newNode
        while current:  # 新节点的下一个还有节点，说明节点还没分配结束
            # 第三趟扫描，开始分节点 current节点在每次前进两个个节点
            newNode.next = current.next
            newNode = newNode.next
            current.next = newNode.next
            current = current.next
        return newHead

    # 返回 RandomListNode
    def Clone(self, pHead):
        if not pHead:
            return
        newHead=RandomListNode(pHead.label)
        newHead.random = pHead.random
        q=newHead
        m={pHead:q,None:None}
        pHead=pHead.next
        while pHead:
            q.next=RandomListNode(pHead.label)
            q=q.next
            q.random=pHead.random
            m[pHead]=q
            pHead=pHead.next
        q=newHead
        while q:
            q.random=m[q.random]
            q=q.next
        return newHead

a=[]
for i in (1,2,3,4,5,3,5,0,2,0):
    a.append(RandomListNode(i))
for i in range(9):
    a[i].next=a[i+1]
    a[i].random=a[random.randint(0,9)]

for x,y in zip(iter(a[0]),iter(Solution().Clone(a[0]))):
    print(x,y)

