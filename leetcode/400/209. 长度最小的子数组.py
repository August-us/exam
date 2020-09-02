from typing import List

'''
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组，并返回其长度。如果不存在符合条件的连续子数组，返回 0。

示例: 

输入: s = 7, nums = [2,3,1,2,4,3]
输出: 2
解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
'''
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        #  拷贝的方法来计算i 到 i+j的和，保存了之前的和，降低了复杂度
        if not nums:return 0
        if max(nums)>=s:return 1
        accSum = nums.copy()
        for i in range(1, len(nums)):
            for j in range(len(nums)-i):
                accSum[j] += nums[i+j]
                if accSum[j] >= s:
                    return i+1
        return 0

    def minSubArrayLen1(self, s: int, nums: List[int]) -> int:
        # 原地的方法实现O(n^2)
        for i in range(1, len(nums)):
            if nums[i] >= s:return 1
            nums[i] += nums[i-1]
        nums += [0]
        for i in range(1, len(nums)):
            for j in range(i-1, len(nums)):
                if nums[j]-nums[j-i] >= s:
                    return i
        return 0

    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        # 创造二分查找的条件，然后对每一个数开头的列表都执行二分查找
        for i in range(1, len(nums)):
            if nums[i] >= s:return 1
            nums[i] += nums[i-1]
        nums += [0]

        res = len(nums)+1
        for i in range(len(nums)-2):
            start,end = i,len(nums)-2
            target = s+nums[i-1]
            while start <= end:
                mid = (start+end) >> 1
                if nums[mid]>=target and nums[mid-1] < target:
                    res = min(res, mid-i+1)
                    break
                elif nums[mid]>=target:
                    end = mid
                else:
                    start = mid+1
            else:
                break
        return 0 if res==len(nums)+1 else res

    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        # 双指针法
        res = len(nums)+1
        sn = j = 0
        for i in range(len(nums)):
            sn += nums[i]

            while sn >= s:
                res = min(res, i-j+1)
                sn -= nums[j]
                j+=1
        return 0 if res==len(nums)+1 else res

# print(Solution().minSubArrayLen1(11, [1,2,3,4,5]))
# print(Solution().minSubArrayLen1(7, [2,3,1,2,4,3]))
print(Solution().minSubArrayLen1(15, [1,2,3,4,5]))