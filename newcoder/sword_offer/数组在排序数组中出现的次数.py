# -*- coding:utf-8 -*-
# 统计一个数字在排序数组中出现的次数
class Solution1:
    def GetNumberOfK(self, data, k):
        # 平铺直叙，调用一次二分查找，然后左右都比较一下
        ind=self.binSearch(data,0,len(data)-1,k)
        res=0
        for i in range(ind,-1,-1):
            if data[i]!=k:
                break
            res+=1
        for i in range(ind+1,len(data)):
            if data[i]!=k:
                break
            res+=1
        return res
    def binSearch(self,data,beg,end,k):
        if beg>end:
            return -1
        mid=(beg+end)>>1
        if data[mid]==k:
            return mid
        if data[mid]<k:
            return self.binSearch(data,mid+1,end,k)
        else:
            return self.binSearch(data,beg,mid-1,k)

class Solution:
    def GetNumberOfK(self, data, k):
        # 因为都是整数，只需要找到 k-0.5需要插入的位置和 k+0.5需要插入的位置，得到的区间一定全是k
        return self.binSearch(data,0,len(data)-1,k+0.5)-self.binSearch(data,0,len(data)-1,k-0.5)
    def binSearch(self,data,beg,end,k):
        while (beg <= end):
            mid = (beg + end) // 2
            if data[mid] <= k:
                beg = mid + 1
            else:
                end = mid - 1
        return beg

print(Solution().GetNumberOfK([1,2,3,3,4],3))
