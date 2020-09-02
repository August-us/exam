from collections import defaultdict
from typing import List

'''
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

说明：

拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
示例 1：

输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
示例 2：

输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
     注意你可以重复使用字典中的单词。
示例 3：

输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false
'''
class Solution139:
    def wordBreak_memory(self, s: str, wordDict: List[str]) -> bool:
        wdict =defaultdict(list)
        memory = set()
        def backtrack(s,start,flag=0):
            if start == len(s):return True
            if start in memory:return False
            for word in wdict[s[start]]:
                if word == s[start:start+len(word)]:
                    if backtrack(s,start+len(word),flag):
                        return True
            if flag==1:
                memory.add(start)
            return False
        for word in wordDict:
            if not backtrack(word,0):
                wdict[word[0]].append(word)
        return True if backtrack(s,0,1) else False

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 动态规划
        wdict =defaultdict(list)
        for word in wordDict:
            wdict[word[0]].append(word)
        dp = [True] + [False] * len(s)
        for start in range(len(s)):
            if not dp[start]:continue
            for word in wdict[s[start]]:
                if word == s[start:start + len(word)]:
                    dp[start+len(word)] = True
        print(dp)
        return dp[-1]

class Solution140:
    '''
    在上一题的基础上需要求出所有的组合方式
    '''''
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # 动态规划
        wdict =defaultdict(list)
        for word in wordDict:
            wdict[word[0]].append(word)
        dp = [True] + [False] * len(s)
        for start in range(len(s)):
            if not dp[start]: continue
            for word in wdict[s[start]]:
                if word == s[start:start + len(word)]:
                    dp[start + len(word)] = True
        if not dp[-1]:return []

        dp =  [[] for i in range(1+len(s))]
        for word in wdict[s[0]]:
            if word == s[:len(word)]:
                dp[len(word)].append([word])
        for start in range(1,len(s)):
            # dp[start-1] = []
            if not dp[start]:continue
            for word in wdict[s[start]]:
                if word == s[start:start + len(word)]:
                    dp[start+len(word)].extend([i+ [word] for i in dp[start]])
        return [' '.join(s) for s in dp[-1]]



s ="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
wordDict = ["aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa","ba"]

print(Solution().wordBreak( s = "catsanddog", wordDict =["cat", "cats", "and", "sand", "dog"]))
# print(Solution().wordBreak_memory( s , wordDict))
