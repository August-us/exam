class Trie(dict):

    def __init__(self, isEnd=False):
        """
        Initialize your data structure here.
        """
        super(Trie, self).__init__()
        self.isEnd = isEnd


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        root = self
        for c in word:
            if c not in root:
                root[c] = Trie()
                root = root[c]
            else:
                root = root[c]
        root.isEnd = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        root = self
        for c in word:
            if c in root:
                root = root[c]
            else:
                return False
        return root.isEnd


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        root = self
        for c in prefix:
            if c in root:
                root = root[c]
            else:
                return False
        return True


'''
持以下两种操作的数据结构：

void addWord(word)
bool search(word)
search(word) 可以搜索文字或正则表达式字符串，字符串只包含字母 . 或 a-z 。 . 可以表示任何一个字母。
'''
class WordDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = {}

    def addWord(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        root = self.children
        for c in word:
            if c not in root:
                child = { }
                root[c] = child
                root = child
            else:
                root = root[c]
        root['#'] ={}

    def match(self, word: str, i =0, root=None) -> bool:
        """
        ·可以匹配任意字符
        """
        root = self.children if i==0 else root
        for i in range(i, len(word)):
            c = word[i]
            if c=='.':
                for c,root in root.items():
                    if self.search(word, i+1, root):
                        return True
                else:return False
            if c in root:
                root = root[c]
            else:
                return False
        return '#' in root

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        root = self.children
        for c in word:
            if c in root:
                root = root[c]
            else:
                return False
        return '#' in root

if __name__ == '__main__':

    methods = ["WordDictionary","addWord","addWord","addWord","addWord","addWord","addWord","addWord","addWord","search","search","search","search","search","search","search","search","search","search"]
    args = [[],["ran"],["rune"],["runner"],["runs"],["add"],["adds"],["adder"],["addee"],["r.n"],["ru.n.e"],["add"],["add."],["adde."],[".an."],["...s"],["....e."],["......."],["..n.r"]]
    obj = WordDictionary()
    for method,arg in zip(methods, args):
        if arg:
            print(obj.__getattribute__(method)(*arg))



