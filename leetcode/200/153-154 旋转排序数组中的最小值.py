from typing import List
'''
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

请找出其中最小的元素。

你可以假设数组中不存在重复元素。

示例 1:

输入: [3,4,5,1,2]
输出: 1
示例 2:

输入: [4,5,6,7,0,1,2]
输出: 0
'''

class Solution:
    def findMin(self, nums: List[int]) -> int:
        start,end = 0,len(nums)-1
        if end >= 0 and nums[end] >= nums[start]: return nums[start]
        while start< end-1:
            mid = (start+end)>>1
            if nums[start] > nums[mid]:
                end = mid
            else:
                start = mid
        return min(nums[start],nums[end])

    def findMin_fast(self, nums):
        if len(nums) == 1:
            return nums[0]

        left = 0
        right = len(nums) - 1

        if nums[right] > nums[0]:
            return nums[0]

        while right >= left:
            mid = (right + left) >> 1

            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            if nums[mid] > nums[0]:
                left = mid + 1
            else:
                right = mid - 1

print(Solution().findMin([2,3,4,5,1]))



'''
数组中可能存在重复的元素
示例 1：

输入: [1,3,5]
输出: 1
示例 2：

输入: [2,2,2,0,1]
输出: 0
'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        start ,end = 0, len(nums) -1
        while start < end:
            mid = (start+end)>>1
            if nums[mid] < nums[end]:
                end = mid
            elif nums[mid] > nums [end]:
                start = mid+1
            else:
                end -= 1
        return nums[start]

