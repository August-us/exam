from typing import List

'''
老师想给孩子们分发糖果，有 N 个孩子站成了一条直线，老师会根据每个孩子的表现，预先给他们评分。

你需要按照以下要求，帮助老师给这些孩子分发糖果：

每个孩子至少分配到 1 个糖果。
相邻的孩子中，评分高的孩子必须获得更多的糖果。
那么这样下来，老师至少需要准备多少颗糖果呢？

示例 1:

输入: [1,0,2]
输出: 5
解释: 你可以分别给这三个孩子分发 2、1、2 颗糖果。
示例 2:

输入: [1,2,2]
输出: 4
解释: 你可以分别给这三个孩子分发 1、2、1 颗糖果。
     第三个孩子只得到 1 颗糖果，这已满足上述两个条件。
'''
class Solution:
    def candy(self, ratings: List[int]) -> int:
        # 一遍扫描，速度很快
        if len(ratings) <2 :return len(ratings)
        res = 1
        up = down = oldSlope =0
        for i in range(1,len(ratings)):
            # slope == 1 代表上坡，==-1代表下坡，为0表示持平
            newSlope = 1 if ratings[i] > ratings[i-1] else -1 if ratings[i] < ratings[i-1] else 0
            if oldSlope > 0 and newSlope ==0 or oldSlope <0 and newSlope >=0:
                # 每一个位置到波峰都是 1...n 所以这里加上n*(n+1)//2 n不包括波峰，波峰为两边共用，最后单独加上
                res += up*(up+1)//2 + down*(down+1)//2 +max(up,down)
                up = 0
                down = 0

            if newSlope > 0:up+=1
            elif newSlope <0:down+=1
            else: res +=1

            oldSlope = newSlope
        res += up * (up + 1) // 2 + down * (down + 1) // 2 + max(up, down)
        return res


    # 记录发的糖果数，两遍扫描，如果比左边的大，就在左边的基础上加1，从右扫描，如果比右边大，就在右边的基础+1
    def candy_twoScan(self, ratings: List[int]) -> int:
        candys = [1] *len(ratings)
        for i in range(1,len(ratings)):
            if ratings[i] > ratings[i-1]:
                candys[i] = candys[i-1] +1
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i] > ratings[i+1]:
                candys[i] = max(candys[i],candys[i+1]+1)
        print(candys)
        return sum(candys)

print(Solution().candy([1,3,2,2,1]))



