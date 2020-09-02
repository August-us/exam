import sys
from typing import List

'''
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

你的目标是使用最少的跳跃次数到达数组的最后一个位置。

示例:

输入: [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
'''
class Solution:
    def jump1(self, nums: List[int]) -> int:
        lenn=len(nums)
        start=0
        end=1
        times=0
        while end<lenn:
            maxPos=0
            for i in range(start,end):
                maxPos=max(maxPos,i+nums[i])
            start=end
            end=maxPos+1
            times+=1
        return times

    def jump(self, nums: List[int]) -> int:
        lenn=len(nums)
        end=times=maxPos=0
        for i in range(lenn-1):# 如果最后一次end==len-1, 这里不需要让i==end之后加1了
            maxPos=max(maxPos,i+nums[i])
            if maxPos>=lenn-1:
                return times+1
            if i==end:
                times+=1
                end=maxPos
        return times

    def jump_froce(self, nums: List[int]) -> int:
        lenn=len(nums)
        steps=[sys.maxsize]*lenn
        steps[0]=0
        for i in range(lenn):
            for j in range(1,min(nums[i]+1,lenn-i)):
                steps[i+j]=min(steps[i+j],steps[i]+1)

        return steps[-1]

a=  [2,3,1,1,4]
print(Solution().jump(a))
