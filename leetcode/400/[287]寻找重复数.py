from typing import List
# 给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。假设只有一个重复的整数，找出
# 这个重复的数。
#
#  示例 1:
#
#  输入: [1,3,4,2,2]
# 输出: 2
#
#
#  示例 2:
#
#  输入: [3,1,3,4,2]
# 输出: 3
#
#
#  说明：
#
#
#  不能更改原数组（假设数组是只读的）。
#  只能使用额外的 O(1) 的空间。
#  时间复杂度小于 O(n2) 。
#  数组中只有一个重复的数字，但它可能不止重复出现一次。
#
#  Related Topics 数组 双指针 二分查找
#  👍 790 👎 0

class Solution_bianraySearch:
    def findDuplicate(self, nums: List[int]) -> int:
        start, end = 1, len(nums) - 1
        while start < end:
            cnt = 0
            mid = (start + end) >> 1
            for i in nums:
                cnt += i <= mid
            if cnt <= mid:
                start = mid + 1
            else:
                end = mid
        return start

    # 第52个测试用例错了，无法调试
    def findDuplicate(self, nums: List[int]) -> int:
        start, end = 1, len(nums) - 1
        while start < end - 1:
            l = r = 0
            mid = (start + end) >> 1
            for i in nums:
                if start <= i <= mid:
                    l += 1
                elif mid < i <= end:
                    r += 1
            if l < r:
                start = mid + 1
            else:
                end = mid
        else:
            if nums.count(start) > 1:
                return start
            else:
                return end


class Solution_bit:
    def findDuplicate(self, nums: List[int]) -> int:
        res = 0
        for i in range(33):
            if len(nums)>>i==0:
                return res
            cur =idea = 0
            for j,n in enumerate( nums):
                idea += j >> i & 1
                cur += n >> i & 1
            res += (cur > idea) << i


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow ,fast = nums[0], nums[nums[0]]

        while slow!=fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        slow = 0
        while slow!=fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
print(Solution().findDuplicate([1, 3, 4, 2, 2]))
print(Solution().findDuplicate([3, 1, 3, 4, 2]))
print(Solution().findDuplicate([2, 2, 2, 2, 2]))
print(Solution().findDuplicate([1, 1]))
print(Solution().findDuplicate([1, 2, 2]))
print(Solution().findDuplicate([7,9,7,4,2,8,7,7,1,5]))
print(Solution().findDuplicate([4, 3, 1, 5, 2, 5]))
