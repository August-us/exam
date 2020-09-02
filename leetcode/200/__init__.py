from algorithm.combinationNumber import factorial


class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 0
        num = 2
        while n:
            res += n//10 * num + (n%10)//5
            num *=2
            n //= 10
        return res

print(Solution().trailingZeroes(30))
print(str(factorial(30))[-10:].count('0'))