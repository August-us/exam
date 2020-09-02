from typing import List
from collections import defaultdict,Counter

'''

给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

示例:

输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
说明：

所有输入均为小写字母。
不考虑答案输出的顺序。
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for string in strs:
            a=tuple(sorted(string))
            res[a].append(string)
        return res.values()

    def groupAnagrams1(self, strs: List[str]) -> List[List[str]]:
        res={}
        for string in strs:
            a=tuple(sorted(string))
            if a in res:
                res[a].append(string)
            else:
                res[a]=[string]
        return res.values()

    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        res={}
        for string in strs:
            a=tuple(Counter(string).items())
            if a in res:
                res[a].append(string)
            else:
                res[a]=[string]
        return res.values()


a= ["hos","boo","nay","deb","wow","bop","bob","brr","hey","rye","eve","elf","pup","bum","iva","lyx","yap","ugh","hem","rod","aha","nam","gap","yea","doc","pen","job","dis","max","oho","jed","lye","ram","pup","qua","ugh","mir","nap","deb","hog","let","gym","bye","lon","aft","eel","sol","jab"]
res=[["sol"],["wow"],["gap"],["hem"],["yap"],["bum"],["ugh","ugh"],["aha"],["jab"],["eve"],["bop"],["lyx"],["jed"],["iva"],["rod"],["boo"],["brr"],["hog"],["nay"],["mir"],["deb","deb"],["aft"],["dis"],["yea"],["hos"],["rye"],["hey"],["doc"],["bob"],["eel"],["pen"],["job"],["max"],["oho"],["lye"],["ram"],["nap"],["elf"],["qua"],["pup","pup"],["let"],["gym"],["nam"],["bye"],["lon"]]
print(sorted(Solution().groupAnagrams1(a)))
print(sorted(res))
