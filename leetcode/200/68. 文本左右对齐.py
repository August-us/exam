from typing import List

'''
给定一个单词数组和一个长度 maxWidth，重新排版单词，使其成为每行恰好有 maxWidth 个字符，且左右两端对齐的文本。

你应该使用“贪心算法”来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格 ' ' 填充，使得每行恰好有 maxWidth 个字符。

要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。

文本的最后一行应为左对齐，且单词之间不插入额外的空格。

说明:

单词是指由非空格字符组成的字符序列。
每个单词的长度大于 0，小于等于 maxWidth。
输入单词数组 words 至少包含一个单词。
示例:

输入:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
输出:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
示例 2:

输入:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
输出:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
解释: 注意最后一行的格式应为 "shall be    " 而不是 "shall     be",
     因为最后一行应为左对齐，而不是左右两端对齐。       
     第二行同样为左对齐，这是因为这行只包含一个单词。
示例 3:

输入:
words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
输出:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]

'''
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        line=[]
        res =[]
        lastWidth=maxWidth
        for word in words:
            if lastWidth<len(word):
                res.append(self.fillSpace(line,lastWidth+1))
                line=[word]
                lastWidth = maxWidth
            else:
                line.append(word)
            lastWidth = lastWidth- 1 - len(word)
        res.append(' '.join(line)+' '*(lastWidth+1))
        return res

    def fillSpace(self, line,lastwidth):
        if len(line)==1:
            return line[0]+' '*lastwidth
        base=lastwidth//(len(line)-1)+1
        front=lastwidth%(len(line)-1)
        for i in range(front):
            line[i]+=' '
        return (' '*base).join(line)


words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
words=["ask","not","what","your","country","can","do","for","you","ask","what","you","can","do","for","your","country"]


res=Solution().fullJustify(words,16)
for line in res:
    print(len(line)==16,line )

for line in ["ask   not   what","your country can","do  for  you ask","what  you can do","for your country"]:
    print(len(line), line)
