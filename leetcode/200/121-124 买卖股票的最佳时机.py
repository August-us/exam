from typing import List

from TestCase import TreeNode, null

'''
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。

注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:

输入: [3,3,5,0,0,3,1,4]
输出: 6
解释: 在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
     随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
示例 2:

输入: [1,2,3,4,5]
输出: 4
解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。   
     注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。   
     因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
示例 3:

输入: [7,6,4,3,1] 
输出: 0 
解释: 在这个情况下, 没有交易完成, 所以最大利润为 0。
'''

'''
通用求解框架，定义两种状态，0,1，分别代表卖出，和持有
dp[i][k][state] 表示第i天 至多k次卖出机会， 此时是持有/卖出我的最大利润 
dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])    dp[i-1][k][1] + prices[i]表示昨天持有，今天卖出
dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])  卖的时候有输入，买的时候就要付出价格，保证卖出的利润一定大于当前持有，最终最大利润就是求卖出
初始化 ： dp[0][k][0] = 0  dp[0][k][1] = -infinity dp[i][0][0] =0 dp[i][0][1] = -infinity             -infinity表示不可能存在的情况

第三题，k = +infinity with cooldown

每次 sell 之后要等一天才能继续交易。只要把这个特点融入上一题的状态转移方程即可：

dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])
解释：第 i 天选择 buy 的时候，要从 i-2 的状态转移，而不是 i-1 。
翻译成代码：

int maxProfit_with_cool(int[] prices) {
    int n = prices.length;
    int dp_i_0 = 0, dp_i_1 = Integer.MIN_VALUE;
    int dp_pre_0 = 0; // 代表 dp[i-2][0]
    for (int i = 0; i < n; i++) {
        int temp = dp_i_0;
        dp_i_0 = Math.max(dp_i_0, dp_i_1 + prices[i]);
        dp_i_1 = Math.max(dp_i_1, dp_pre_0 - prices[i]);
        dp_pre_0 = temp;
    }
    return dp_i_0;
}
第四题，k = +infinity with fee

每次交易要支付手续费，只要把手续费从利润中减去即可。改写方程：

dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i] - fee)
解释：相当于买入股票的价格升高了。
在第一个式子里减也是一样的，相当于卖出股票的价格减小了。
直接翻译成代码：

int maxProfit_with_fee(int[] prices, int fee) {
    int n = prices.length;
    int dp_i_0 = 0, dp_i_1 = Integer.MIN_VALUE;
    for (int i = 0; i < n; i++) {
        int temp = dp_i_0;
        dp_i_0 = Math.max(dp_i_0, dp_i_1 + prices[i]);
        dp_i_1 = Math.max(dp_i_1, temp - prices[i] - fee);
    }
    return dp_i_0;
}

第六题，k = any integer

有了上一题 k = 2 的铺垫，这题应该和上一题的第一个解法没啥区别。但是出现了一个超内存的错误，原来是传入的 k 值会非常大，dp 数组太大了。现在想想，交易次数 k 最多有多大呢？

一次交易由买入和卖出构成，至少需要两天。所以说有效的限制 k 应该不超过 n/2，如果超过，就没有约束作用了，相当于 k = +infinity。这种情况是之前解决过的。

直接把之前的代码重用：

int maxProfit_k_any(int max_k, int[] prices) {
    int n = prices.length;
    if (max_k > n / 2) 
        return maxProfit_k_inf(prices);

    int[][][] dp = new int[n][max_k + 1][2];
    for (int i = 0; i < n; i++) 
        for (int k = max_k; k >= 1; k--) {
            if (i - 1 == -1) { /* 处理 base case */ }
            dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i]);
            dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i]);     
        }
    return dp[n - 1][max_k][0];
}

'''


class Solution:
    def maxProfit_recur(self, prices: List[int], n=2, start=0) -> int:
        print(n, start)
        if n == 0 or start >= len(prices):
            return 0
        maxprofit = 0

        if n == 1:
            minprice = float('inf')
            for price in prices[start:]:
                maxprofit = max(price - minprice, maxprofit)
                minprice = min(price, minprice)
        else:
            curV = 0
            for i in range(start + 1, len(prices)):
                if prices[i] > prices[i - 1]:
                    curV += prices[i] - prices[i - 1]
                else:
                    if curV > 0:
                        maxprofit = max(maxprofit, curV + self.maxProfit_recur(prices, n - 1, i))
                    curV += prices[i] - prices[i - 1]
                    if curV < 0:
                        return max(maxprofit, self.maxProfit_recur(prices, n, i))
            maxprofit = max(maxprofit, curV)
        return maxprofit

    def maxProfit(self, prices: List[int]) -> int:
        dp10 = 0
        dp11 = -float('inf')
        dp20 = 0
        dp21 = -float('inf')
        for p in prices:
            dp10 = max(dp10, dp11 + p)
            dp11 = max(dp11, -p)
            dp20 = max(dp20, dp21 + p)
            dp21 = max(dp21, dp10 - p)
        return dp20


class Solution124:
    '''
    给定一个非空二叉树，返回其最大路径和。
    本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。
    示例 1:

    输入: [1,2,3]

           1
          / \
         2   3

    输出: 6
    示例 2:

    输入: [-10,9,20,null,null,15,7]

       -10
       / \
      9  20
        /  \
       15   7

    输出: 42
    '''''

    def maxPathSum_down(self, root: TreeNode) -> int:
        # 理解错了题目，以为同一分支上才算是路径,这样就可以把这个问题转换成最大子串和的非递归形式
        stack = [[None, -float('inf')]]
        maxSum = 0
        while root or len(stack) > 1:
            if root:
                while root:
                    stack.append([root, max(0, root.val, stack[-1][1] + root.val)])
                    maxSum = max(maxSum, stack[-1][1])
                    root = root.left

            else:
                root = stack[-1][0].right
                if not root:
                    pre, _ = stack.pop()
                    while len(stack) > 1 and stack[-1][0].right == pre:
                        pre, _ = stack.pop()
        return maxSum

    def maxPathSum(self, root: TreeNode) -> int:
        maxPath = -float('inf')

        def maxPathCore(root: TreeNode) -> int:
            if not root:
                return 0
            nonlocal maxPath
            left = maxPathCore(root.left)
            right = maxPathCore(root.right)
            maxPath = max(maxPath, left + right + root.val)
            return max(left + root.val, right + root.val, 0)

        maxPathCore(root)
        return maxPath


root = TreeNode.createTree([-10])
print(Solution124().maxPathSum(root))

