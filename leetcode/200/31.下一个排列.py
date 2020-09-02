from typing import List
'''
实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
必须原地修改，只允许使用额外常数空间。
以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

思路：找到第一个数字比它右边的数字小，然后右边肯定是降序排列，右边翻转，找到当前数字的右边的恰好比它大的数字，两者交换
'''

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        if not nums:return
        for i in range(len(nums)-2,-1,-1):
            if nums[i+1]>nums[i]:
                nums[i+1:]=reversed(nums[i+1:])
                for j in range(i+1,len(nums)):
                    if nums[i]<nums[j]:
                        nums[i],nums[j]=nums[j],nums[i]
                        return
        else:
            nums.reverse()
nums=[1,3,2]
Solution().nextPermutation(nums)
print(nums)
