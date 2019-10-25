# -*- coding: utf-8 -*-
import sys
def merge(nums, first, middle, last):
    ''''' merge '''
    # 切片边界,左闭右开并且是了0为开始
    lnums = nums[first:middle+1]
    rnums = nums[middle+1:last+1]
    lnums.append(sys.maxint)
    rnums.append(sys.maxint)
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
        middle = (first + last)/2
        merge_sort(nums, first, middle)
        merge_sort(nums, middle+1, last)
        merge(nums, first, middle,last)
def select_sort(a):
    ''''' 选择排序
    每一趟从待排序的数据元素中选出最小（或最大）的一个元素，
    顺序放在已排好序的数列的最后，直到全部待排序的数据元素排完。
    选择排序是不稳定的排序方法。
    '''
    a_len=len(a)
    for i in range(a_len):#在0-n-1上依次选择相应大小的元素
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


def shell_sort(a):
    ''''' shell排序
    '''
    a_len=len(a)
    gap=a_len/2#增量
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
        gap/=2


def partition2(A,start,end):
    privot=A[start]
    while start<end:
        while start<end and A[end]>=privot:
            end-=1
        A[start], A[end] = A[end], A[start]
        while start<end and A[start]<=privot:
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
        q = partition2(A, p, r)
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, r)

if __name__=="__main__":
    A = [5, -4, 6, 3, 7, 11, 1, 2]
    bubble_sort(A)
    # insert_sort(A)
    print(A)

