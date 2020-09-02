import math


class Solution:
    def __init__(self):
        self.prime = [2, 3, 5, 7, 11]

    def appendPrime(self, n):
        for i in range(self.prime[-1]+2, n , 2):
            sqr = int(math.sqrt(i))
            for j in self.prime:
                if j > sqr:
                    self.prime.append(i)
                    break
                elif i%j == 0:
                    break


    def countPrimes(self, n: int) -> int:
        self.appendPrime(n)
        start, end = 0, len(self.prime)-1
        print(self.prime)

        while start <= end:
            mid = (start+end)>>1
            if n == self.prime[mid]:
                return mid
            if n < self.prime[mid]:
                end = mid -1
            else:
                start = mid + 1
        return start

    def sieve(self,  n: int) -> int:
        # 挖空法来计算素数
        prime = [1 for i in range(n-2)]
        res, cur = 0, 2
        while cur < n:
            if prime[cur-2]:
                for i in range(cur*2, n, cur):
                    prime[i-2] = 0
                res +=1
            cur += 1
        return res



s = Solution()
print(s.sieve(10))
print(s.countPrimes(5))



