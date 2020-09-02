from collections import defaultdict
from typing import List


'''
在整数数组 nums 中，是否存在两个下标 i 和 j，使得 nums [i] 和 nums [j] 的差的绝对值小于等于 t ，且满足 i 和 j 的差的绝对值也小于等于 ķ 。

如果存在则返回 true，不存在返回 false。

 

示例 1:

输入: nums = [1,2,3,1], k = 3, t = 0
输出: true
示例 2:

输入: nums = [1,0,1,1], k = 1, t = 2
输出: true
示例 3:

输入: nums = [1,5,9,1,5,9], k = 2, t = 3
输出: false
'''
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if k==0 or t<0:
            return False
        if t==0:
            window = set()
            for i in range(len(nums)):
                if nums[i] in window:
                    return True
                if i >= k:
                    window.remove(nums[i - k])
                window.add(nums[i])
            return False
        bucket = defaultdict(lambda:set())
        for i in range(len(nums)):
            if bucket.get(nums[i]//t, ()):
                return True
            for n in bucket.get(nums[i]//t-1, ()):
                if abs(n - nums[i]) <=t :
                    return True
            for n in bucket.get(nums[i]//t+1,()):
                if abs(n - nums[i]) <=t :
                    return True
            bucket[nums[i]//t].add(nums[i])
            if i>=k:
                bucket[nums[i-k]//t].remove(nums[i-k])
        return False

    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        # 直接列出当前位置不能出现的所有的数字，如果出现了就返回
        # 似乎只能是对每一个状态求一个不能取值的哈希表
        if t < 0 or not k or not nums:
            return False

        if k == 1:
            for i in range(len(nums) - 1):
                if abs(nums[i] - nums[i + 1]) <= t:
                    return True
            return False

        if not t:
            dct = {}
            for inx, i in enumerate(nums):
                if i in dct:
                    if inx - dct[i] <= k:
                        return True
                dct[i] = inx
            return False

        lst = []
        i = nums[0]
        lst.append(sum([(i - j, i + j) for j in range(t + 1)], ()))

        for i in nums[1:]:
            if i in set(sum(lst, ())):
                return True
            lst.append(sum([(i - j, i + j) for j in range(t + 1)], ()))
            lst = lst[-k:]

        return False


# print(Solution().containsNearbyAlmostDuplicate(nums = [1,5,9,1,5,9], k = 5, t = 3))
print(Solution().containsNearbyAlmostDuplicate([3,6,0,4],
2,
2))


'''
python不能使用排序二叉树
'''