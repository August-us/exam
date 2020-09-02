from typing import List

'''
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,0,1,2,2,5,6] 可能变为 [2,5,6,0,0,1,2] )。

编写一个函数来判断给定的目标值是否存在于数组中。若存在返回 true，否则返回 false。

示例 1:

输入: nums = [2,5,6,0,0,1,2], target = 0
输出: true
示例 2:

输入: nums = [2,5,6,0,0,1,2], target = 3
输出: false
进阶:

这是 搜索旋转排序数组 的延伸题目，本题中的 nums  可能包含重复元素。
这会影响到程序的时间复杂度吗？会有怎样的影响，为什么？
'''
class Solution:
    def search(self, nums: List[int], target: int) -> bool:


        if not nums:return False
        start,end=0,len(nums)-1
        while end>0 and nums[start]==nums[end] :end-=1
        if nums[end]==target:return True
        while start<=end:
            while start<end and nums[start + 1] == nums[start]: start += 1
            while end>start and nums[end- 1] == nums[end]: end-= 1
            mid=(start+end)>>1
            if nums[mid]==target or nums[start]==target:
                return True
            elif nums[start]<target:
                if nums[mid]<target and nums[mid]>=nums[start]:
                    start=mid+1
                else:
                    end = mid - 1
            else:
                if nums[mid]<target or nums[mid]>nums[start]:
                    start=mid+1
                else :
                    end = mid - 1

        return False




nums =[[3,1,2,2,2],
[15,16,19,20,25,1,3,4,5,7,10,14]]
target = [1,25]
res=[True,True]
for n,t,r in zip(nums,target,res):
    print(r,Solution().search(n,t))
    # input()
