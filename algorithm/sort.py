# -*- coding: utf-8 -*-
import sys
from typing import List

from TestCase import ListNode

maxint=9223372036854775807

def merge(nums, first, middle, last):
    ''''' merge '''
    # 切片边界,左闭右开并且是了0为开始
    lnums = nums[first:middle+1]
    rnums = nums[middle+1:last+1]
    lnums.append(maxint)
    rnums.append(maxint)
    l = 0
    r = 0
    for i in range(first, last+1):
        if lnums[l] < rnums[r]:
            nums[i] = lnums[l]
            l+=1
        else:
            nums[i] = rnums[r]
            r+=1
def merge_sort(nums, first, last):
    ''''' merge sort
    merge_sort函数中传递的是下标，不是元素个数
    '''
    if first < last:
        middle = int((first + last)/2)
        merge_sort(nums, first, middle)
        merge_sort(nums, middle+1, last)
        merge(nums, first, middle,last)

# 链表的归并排序，非递归算法
def mergesort_List(head: ListNode) -> ListNode:
    def merge(head,q, qk,k):
        left = right = k
        while left and right and qk:
            if q.val > qk.val:
                head.next = qk
                qk = qk.next
                right -= 1
            else:
                head.next = q
                q = q.next
                left -=1
            head = head.next
        head.next = None
        while left and q:
            head.next = q
            q = q.next
            head = head.next
            left -=1
        while right and qk:
            head.next = qk
            qk = qk.next
            right -= 1
            head = head.next
        head.next = qk
        return head

    k, length = 1,0
    p = head
    while p:
        length += 1
        p = p.next

    newHead = ListNode('')
    newHead.next = head

    while k < length:
        head = newHead
        while head.next:
            q = qk = head.next
            for i in range(k):
                if not qk:
                    break
                qk = qk.next
            head = merge(head,q,qk,k)
        k *= 2
    return newHead.next


# 链表的归并排序，递归算法
def sortList(head: ListNode) -> ListNode:
    def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2:
            if l1.val > l2.val: l1, l2 = l2, l1
            l1.next = mergeTwoLists(l1.next, l2)
        return l1 or l2
    if not (head and head.next): return head
    pre, slow, fast = None, head, head
    while fast and fast.next: pre, slow, fast = slow, slow.next, fast.next.next
    pre.next = None
    return mergeTwoLists(*map(sortList, (head, slow)))


def select_sort(a):
    ''''' 选择排序
    每一趟从待排序的数据元素中选出最小（或最大）的一个元素，
    顺序放在已排好序的数列的最后，直到全部待排序的数据元素排完。
    选择排序是不稳定的排序方法。
    '''
    a_len=len(a)
    for i in range(a_len-1):#在0-n-1上依次选择相应大小的元素
        min_index = i#记录最小元素的下标
        for j in range(i+1, a_len):#查找最小值
            if(a[j]<a[min_index]):
                min_index=j
        if min_index != i:#找到最小元素进行交换
            a[i],a[min_index] = a[min_index],a[i]


def bubble_sort(alist):
    n = len(alist)
    for j in range(n - 1):
        count = 0
        for i in range(0, n - 1 - j):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                count += 1
        if 0 == count:
            break


def insert_sort(array):
    for i in range(1, len(array)):
        if array[i - 1] > array[i]:
            temp = array[i]  # 当前需要排序的元素
            index = i  # 用来记录排序元素需要插入的位置
            while index > 0 and array[index - 1] > temp:
                array[index] = array[index - 1]  # 把已经排序好的元素后移一位，留下需要插入的位置
                index -= 1
            array[index] = temp

def bin_inser(array):
    for i in range(1, len(array)):
        if array[i - 1] > array[i]:
            temp = array[i]  # 当前需要排序的元素
            index = i  # 用来记录排序元素需要插入的位置
            beg, end = 0, i-1
            while (beg <= end):
                mid = (beg + end) // 2
                if array[mid] <= temp:
                    beg = mid + 1
                else:
                    end = mid - 1
            while index > beg:
                array[index] = array[index - 1]  # 把已经排序好的元素后移一位，留下需要插入的位置
                index -= 1
            array[index] = temp

def shell_sort(a):
    ''''' shell排序
    '''
    a_len=len(a)
    gap=a_len//2#增量
    while gap>0:
        for i in range(a_len):#对同一个组进行选择排序
            m=i
            j=i+1
            while j<a_len:
                if a[j]<a[m]:
                    m=j
                j+=gap#j增加gap
            if m!=i:
                a[m],a[i]=a[i],a[m]
        gap//=2


def partition2(A,start,end):
    pivot=A[start]
    while start<end:
        while start<end and A[end]>=pivot:
            end-=1
        A[start], A[end] = A[end], A[start]
        while start<end and A[start]<=pivot:
            start+=1
        A[start],A[end]=A[end],A[start]
    return start


def partition(A, p, r):
    x = A[r]
    i = p - 1
    j = p
    while j < r:
        if A[j] < x:
            i += 1
            A[i], A[j] = A[j], A[i]
        j += 1
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, r)

# 链表的快速排序
def qucik_sort_list(head):
    def partition(start, end):
        node = start.next.next
        pivotPrev = start.next
        pivotPrev.next = end
        pivotPost = pivotPrev
        while node != end:
            temp = node.next
            if node.val > pivotPrev.val:
                node.next = pivotPost.next
                pivotPost.next = node
            elif node.val < pivotPrev.val:
                node.next = start.next
                start.next = node
            else:
                node.next = pivotPost.next
                pivotPost.next = node
                pivotPost = pivotPost.next
            node = temp
        return [pivotPrev, pivotPost]

    def quicksort(start, end):
        if start.next != end:
            prev, post = partition(start, end)
            quicksort(start, prev)
            quicksort(post, end)

    newHead = ListNode(0)
    newHead.next = head
    quicksort(newHead, None)
    return newHead.next


def findKthSmallNumber(array,k):
    if k>=len(array) or k<0:
        return
    start=0
    end=len(array)-1
    i=partition(array,start,end)
    while (i!=k):
        if i>k:
            end=i-1
        else:
            start=i+1
        i = partition(array, start, end)
    return array[i]

def countingSort(A):
    from collections import Counter
    index=Counter(A)
    pre=0
    for k,v in sorted(index.items()):
        index[k]+=pre
        pre=index[k]
    # B=A[::-1]
    for i in A[::-1]:
        index[i]-=1
        A[index[i]]=i

def bucket_sort(A,high,low,bucket):
    bucketWidth=(high-low)//bucket
    buckets=[[] for i in range(bucket)]
    for i in A:
        buckets[(i-low)//bucketWidth].append(i)
    cur=0
    A.clear()
    for bucket in buckets:
        A.extend(sorted(bucket))

def radisSort(A,base=10,width=None):
    if not width:
        width=len(str(max(A)))
    for i in range(width):
        times=[0]*base
        mod=base**i
        for num in A:
            times[num//mod%base]+=1
        for i in range(1,base):
            times[i]+=times[i-1]
        for num in A[::-1]:
            times[num//mod%base] -= 1
            A[times[num//mod%base]] = num


# 二分查找找临界点
def binSearch(citations: List[int]) -> int:
    citations = list(reversed(citations))
    start, end = 0, len(citations)
    def check(i):
        if i < len(citations):
            return citations[i] < i
        return True
    while start < end:
        mid = (start+end)>>1
        if citations[mid] >= mid+1 and check(mid+1):
            return mid+1
        elif citations[mid] < mid+1:
            end = mid
        else:
            start = mid+1 # 找临界点，一般start = mid+1而end不减1
    return start

if __name__=="__main__":
    A = [5, -4, 6, 3, 7, 11, 1, 2]
    # quick_sort(A,0,len(A)-1)
    print(findKthSmallNumber(A,5))
    quick_sort(A,0,len(A)-1)
    print(A)
    A=[21,11,51,16,56,26,42,32,82,15,55,86]
    radisSort(A,10,2)
    print(A)
    print(-123%10)
    # insert_sort(A)

