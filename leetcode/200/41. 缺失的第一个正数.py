from typing import List

'''
给定一个未排序的整数数组，找出其中没有出现的最小的正整数。

示例 1:

输入: [1,2,0]
输出: 3
示例 2:

输入: [3,4,-1,1]
输出: 2
示例 3:

输入: [7,8,9,11,12]
输出: 1
'''
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        j,n=0,len(nums)
        while j<n:
            i=nums[j]
            if i>0 and i<=n and j+1!=i and nums[i-1]!=i:
                nums[i-1],nums[j]=nums[j],nums[i-1]
                continue
            j+=1

        for i,num in enumerate(nums):
            if num!=i+1:
                return i+1
        return n+1

    def firstMissingPositive1(self, nums: List[int]) -> int:
        n=len(nums)
        appear=[0]*n
        for num in nums:
            if num>0 and num<=n:
                appear[num-1]+=1
        for i,num in enumerate(appear):
            if num==0:
                return i+1
        return n+1

    def firstMissingPositive_set(self, nums: List[int]) -> int:
        s=set()
        n=len(nums)
        for num in nums:
            if num >0 and num<=n:
                s.add(num)
        for i in range(1,n+2):
            if i not in s:
                return i

print(Solution().firstMissingPositive(
[1,2,0]))


def firstMissingPositive(nums: List[int]) -> int:
    j, n = 0, len(nums)
    while j < n:
        i = nums[j]
        if i > 0 and i <= n and j + 1 != i and nums[i - 1] != i:
            nums[i - 1], nums[j] = nums[j], nums[i - 1]
            continue
        j += 1

    for i, num in enumerate(nums):
        if num != i + 1:
            return i + 1
    return n + 1

