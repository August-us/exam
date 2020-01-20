# -*- coding:utf-8 -*-
'''
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一
个二维数组和一个整数，判断数组中是否含有该整数。
'''
class Solution:
    # array 二维列表
    def Find(self,target,  array):
        return self.binary_find(array,target)
    def binary_find(self, array,target):
        print(array)
        m = len(array)
        if m==0:
            return False
        n=len(array[0])
        if n==0:
            return False
        if target == array[m // 2][ n // 2]:
            return True
        if target < array[m // 2][ n // 2]:
            print(1,array[m // 2][ n // 2])
            a=[]
            for i in array[m // 2:]:
                a.append(i[:n // 2])
            # return self.binary_find(array[:m // 2],target) or self.binary_find(array[m // 2:][:n // 2],target)
            return self.binary_find(array[:m // 2], target) or self.binary_find(a, target)

        else:
            print(2,array[m // 2][ n // 2])
            a=[]
            for i in array[m//2+1:]:
                a.append(i[:n//2+1])
            b=[]
            for i in array:
                b.append(i[n//2+1:])
            # return self.binary_find(array[m//2+1:][:n//2+1],target) or self.binary_find(array[:][n//2+1:],target)
            return self.binary_find(a,target) or self.binary_find(b,target)

class SolutionForce():
    def Find(self, target, arrays):
        for array in arrays:
            if self.binaryFind1d(array, target, 0, len(array) - 1):
                return True
        return False

    def binaryFind1d(self,array1d,target,beg,end):
        # 这里只需要判断是否找到，一般二分查找返回的是索引
        mid=(beg+end)>>1 # 右移一位，相当于除二
        if target==array1d[mid]:
            return True
        if target<array1d:
            return self.binaryFind1d(array1d,target,beg,mid-1)
        else:
            return self.binaryFind1d(array1d,target,mid+1,end)
class Solution1:
    # array 二维列表
    def Find(self, target, array):
        return self.binary_find(array, target, 0, len(array) - 1, 0, len(array[0]) - 1)

    def binary_find(self, array, target, up, down, left, right):
        if down < up or right < left:
            return False
        h = (up + down) // 2
        v = (left + right) // 2
        if target == array[h][v]:
            return True
        if target < array[h][v]:
            return self.binary_find(array, target, up, h - 1, left, right) or self.binary_find(array, target, h, down,left, v - 1)
        else:
            return self.binary_find(array, target, h + 1, down, left, v) or self.binary_find(array, target, up, down,v + 1, right)

class Solution_froce:
    # array 二维列表
    def Find(self, target, array):
        for i in range(len(array)):
            if target in array[i]:
                return True
        return False


class SolutionO_n:
    def Find(self,target,array):
        h,v=len(array)-1,0
        while(h>=0 and v<len(array[0])):
            if array[h][v]==target:
                return True
            if array[h][v] > target:
                h-=1
            else:
                v+=1
        return False

Solution1().Find(5,[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]])

print(SolutionO_n().Find(28,[[1,3,4,9,10],[2,5,11,12,15],[6,8,13,14,16],[17,19,21,23,25],[18,20,22,24,26]]))

