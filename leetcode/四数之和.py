from typing import List
'''
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。
注意：答案中不可以包含重复的四元组。
示例：给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,
]
'''
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n=len(nums)
        res=[]
        nums.sort()
        for i in range(n-3):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,n-2):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                start=j+1
                end=n-1
                while start<end:
                    if nums[i]+nums[j]+nums[start]+nums[end]==target:
                        res.append([nums[i],nums[j],nums[start],nums[end]])
                        while start<end-1 and nums[start]==nums[start+1]:
                            start+=1
                        while start < end - 1 and nums[end] == nums[end - 1]:
                            end -= 1
                    if nums[i]+nums[j]+nums[start]+nums[end]<target:
                        start+=1
                    else:
                        end-=1

        return res
nums = [5,5,3,5,1,-5,1,-2]
target = 4
print(Solution().fourSum(nums,target))