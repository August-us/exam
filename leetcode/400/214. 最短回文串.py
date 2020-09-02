class Solution:
    # 时间复杂度: O(n^2)
    def shortestPalindrome(self, s: str) -> str:
        for i in range(len(s)):
            mid = (i + len(s)) // 2 -i
            if (i+len(s)) &1:
                if s[:mid] == s[(mid<<1):mid:-1]:
                    return s[:mid:-1]+s[mid:]
            elif s[:mid]==s[(mid<<1)-1:mid-1:-1]:
                return s[:mid-1:-1]+s[mid:]
        return ''

    def shortestPalindrome(self, ss: str) -> str:
        s = ss + '#' + ss[::-1]
        next = [0 for i in range(len(s))]
        for i in range(1, len(s)):
            t = next[i-1]
            while t>0 and s[t]!=s[i]:
                t = next[t-1]
            t+=s[t]==s[i]
            next[i] = t
        print(s[len(s)//2-1:next[-1]-1:-1])
        return s[len(s)//2-1:next[-1]-1:-1] + s[:len(s)//2]

    def shortestPalindrome_kmp(self, s: str) -> str:
        next = [0 for i in range(len(s))]
        for i in range(1, len(s)):
            t = next[i-1]
            while t>0 and s[t]!=s[i]:
                t = next[t-1]
            t += s[t]==s[i]
            next[i] = t
        t = 0
        for i in range(1, len(s)+1):
            while t>0 and s[t]!=s[-i]:
                t = next[t-1]
            t += s[t]==s[-i]
        return s[:t-1:-1] + s
a = "aacecaaa"

print(Solution().shortestPalindrome_kmp(a))

