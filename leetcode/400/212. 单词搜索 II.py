from typing import List

from algorithm.Trie import Trie

'''
给定一个二维网格 board 和一个字典中的单词列表 words，找出所有同时在二维网格和字典中出现的单词。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。

示例:

输入: 
words = ["oath","pea","eat","rain"] and board =
[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]

输出: ["eat","oath"]
'''
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        dic = Trie()
        for word in words:
            dic.insert(word)

        def dfs(i, j, root, path):
            if root.isEnd:
                res.append(''.join(path))
                root.isEnd = False
            if 0 <= i < len(board) and 0<= j < len(board[0]) and not visited[i][j] and board[i][j] in root:
                path.append(board[i][j])
                visited[i][j] = True
                for loc in [(i-1,j), (i+1,j), (i,j-1),(i,j+1)]:
                    if dfs(*loc, root[board[i][j]],path):
                        del root[board[i][j]]
                        break
                path.pop()
                visited[i][j] = False
            return not root

        res = []
        if not board[0]:return res
        visited = [[False for i in range(len(board[0]))] for j in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i,j, dic, [])
        print(dic)
        return res


print(Solution().findWords( words = ["oath","pea","eat","rain"], board =
[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
))
print(Solution().findWords([["a","b"]]
,["ba"]))

