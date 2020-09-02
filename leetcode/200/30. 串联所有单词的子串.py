from typing import List
'''
给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。
注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。
示例 1：
输入：
  s = "barfoothefoobarman",
  words = ["foo","bar"]
输出：[0,9]
解释：
从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
输出的顺序不重要, [9,0] 也是有效答案。
示例 2：
输入：
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
输出：[]
'''
class Solution1:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words or len(words[0]) == 0:
            return []
        lenw = len(words[0])
        lens = len(s)
        t=lens - lenw*len(words)
        res = []
        start = 0
        while start <=t :
            # if s[start:start + lenw] in words:
            w=words.copy()
            end=start
            while end+lenw<=lens and s[end:end+lenw] in w:
                w.remove(s[end:end+lenw])
                end+=lenw
            else:
                if len(w)==0:
                    res.append(start)
            start +=1

        return res


class Solution:
    '''
    滑动窗口，每次往前走一个单词的长度，但是一共要走一个单词的长度次
    '''
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        from collections import Counter
        if not s or not words:return []
        one_word = len(words[0])
        word_num = len(words)
        n = len(s)
        if n < one_word*word_num:return []
        words = Counter(words)
        res = []
        for i in range(0, one_word):
            cur_cnt = 0
            left = i
            right = i
            cur_Counter = Counter()
            while right + one_word <= n:
                w = s[right:right + one_word]
                right += one_word
                if w not in words:
                    left = right
                    cur_Counter.clear()
                    cur_cnt = 0
                else:
                    cur_Counter[w] += 1
                    cur_cnt += 1
                    while cur_Counter[w] > words[w]:
                        left_w = s[left:left+one_word]
                        left += one_word
                        cur_Counter[left_w] -= 1
                        cur_cnt -= 1
                    if cur_cnt == word_num :
                        res.append(left)
        return res


s = "a"*1000
w=["aaa"]*10
print(Solution().findSubstring(s,w))
# print(len(s),len(w))
