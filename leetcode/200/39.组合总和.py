from typing import List
'''
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的数字可以无限制重复被选取。

说明：
所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 
示例 1:
输入: candidates = [2,3,6,7], target = 7,
所求解集为:
[
  [7],
  [2,2,3]
]

示例 2:
输入: candidates = [2,3,5], target = 8,
所求解集为:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
'''

class Solution1:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort(reverse=True)
        if not candidates or target<candidates[-1]:
            return []
        return self.combinationSumCore(candidates,target)

    def combinationSumCore(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        if not candidates or target < candidates[-1]:
            return [[]]
        for i, n in enumerate(candidates):
            for j in range(1,target // n+1):
                res.extend([[n] * j + x for x in self.combinationSumCore(candidates[i + 1:], target - n * j) if x])
            if target%n==0:
                res.append([n]*(target//n))
        return res


# 提交的记录说明，从大的数开始计算可以更快的让递归终止条件结束
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort(reverse=True)
        if not candidates or target<candidates[-1]:
            return []
        return self.combinationSumCore(candidates,0,target)

    def combinationSumCore(self, candidates: List[int],start:int, target: int) -> List[List[int]]:
        res = []
        if start==len( candidates) or target < candidates[-1]:
            return [[]]
        for i in range(start,len(candidates)):
            n=candidates[i]
            if target%n==0:
                res.append([n]*(target//n))
            for j in range(1,(target-1) // n+1):
                res.extend([[n] * j + x for x in self.combinationSumCore(candidates,i+1, target - n * j) if x])
        return res


candidates =[2,3,5]
target=8
print(Solution().combinationSum(candidates,target))