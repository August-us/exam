from collections import defaultdict
from typing import List

'''
给定一个未排序的整数数组，找出最长连续序列的长度。

要求算法的时间复杂度为 O(n)。

示例:

输入: [100, 4, 200, 1, 3, 2]
输出: 4
解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。
'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        通过合并区间的方式，有点浪费空间
        '''''
        nums = set(nums)
        sequence = defaultdict(list)
        for i in nums:
            if i-1 in sequence and i+1 in sequence:
                sequence[sequence[i-1][0]].extend([i] + sequence[i+1])
                sequence[sequence[i+1][-1]] = sequence[sequence[i-1][0]]

            elif i-1 in sequence:
                sequence[sequence[i-1][0]].append(i)
                sequence[i] = sequence[sequence[i-1][0]]

            elif i+1 in sequence:
                sequence[sequence[i + 1][-1]].insert(0,i)
                sequence[i] = sequence[sequence[i + 1][-1]]

            else:
                sequence[i] = [i]
            if i-1 in sequence and sequence[i-1][0] != i-1:
                del sequence[i-1]

            if i+1 in sequence and sequence[i+1][-1] != i+1:
                del sequence[i+1]
        longest = 0
        for k,v in sequence.items():
            if len(v) > longest:
                longest = len(v)
        return longest

    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        maxLength=0
        while nums:
            a = nums.pop()
            l = a-1
            u = a+1
            while l in nums:
                nums.remove(l)
                l -= 1

            while u in nums:
                nums.remove(u)
                u +=1
            maxLength = max(u-l-1,maxLength)
        return maxLength
print(Solution().longestConsecutive( [-7,-1,3,-9,-4,7,-3,2,4,9,4,-9,8,-7,5,-1,-7]))
print(sorted( [-7,-1,3,-9,-4,7,-3,2,4,9,4,-9,8,-7,5,-1,-7]))
