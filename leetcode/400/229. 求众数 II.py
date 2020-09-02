from collections import defaultdict
from typing import List


'''
给定一个大小为 n 的数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。

说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1)。

示例 1:

输入: [3,2,3]
输出: [3]
示例 2:

输入: [1,1,1,3,3,2,2,2]
输出: [1,2]
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        aready = {}
        second = defaultdict(lambda: 0)
        for i in nums:
            if i not in aready:
                if len(aready) == 2:
                    deleted = []
                    for i in aready.keys():
                        if aready[i] == 1:
                            deleted.append(i)
                        else:
                            aready[i] -= 1
                    for i in deleted:
                        del aready[i]
                else:
                    aready[i] = 1
            else:
                aready[i] += 1
        for i in nums:
            if i in aready:
                second[i] +=1
        res = []
        for k,v in second.items():
            if v> len(nums)//3:
                res.append(k)
        return res

print(Solution().majorityElement(
[3,2,3]))
