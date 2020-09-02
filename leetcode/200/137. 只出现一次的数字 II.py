from functools import reduce
from typing import List

'''
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现了三次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,3,2]
输出: 3
示例 2:

输入: [0,1,0,1,0,1,99]
输出: 99
'''
class Solution:
    def singleNumber_bits(self, nums: List[int]) -> int:
        bits = [0]*32
        for i in nums:
            for j in range(32):
                bits[j]+= (i >> j) &1
        if bits[-1]%3==1:
            return -1 - reduce(lambda x,y:(x<<1)+(1-y%3),bits[len(bits)-2::-1],0)
        return  reduce(lambda x,y:(x<<1)+y%3,bits[::-1],0)

    def singleNumber(self, nums: List[int]) -> int:
        seen_once = seen_twice = 0

        for num in nums:
            # 使用位运算，如果出现第一次，在记录在seen_once中，如果出现两次，从seen_once删除，加入seen_twice中，如果出现三次，不加入seen_one 并且从seen_twice删除
            seen_once = ~seen_twice & (seen_once ^ num)
            seen_twice = ~seen_once & (seen_twice ^ num)


        return seen_once
        # return reduce(lambda x,y:(),nums,(0,0))[0]




print(Solution().singleNumber( [-2,-2,-2,-2,-2,-4,-2]) )