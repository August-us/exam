from typing import List

from collections import defaultdict


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        for i in range(len(s)):
            if s[i] == '(':
                s = ''.join([s[j] for j in range(i) if s[j]!=')']) + s[i:]
                break
        else:
            return [''.join([j for j in s if j!=')'])]
        for i in reversed(range(len(s))):
            if s[i] == ')':
                s = s[:i+1] + ''.join([s[j] for j in range(i+1, len(s)) if s[j]!='('])
                break
        else:
            return [''.join([j for j in s if j!='('])]
        left, right, deletes = [],[],[0]
        l = r =0
        for i,c in enumerate(s):
            if c=='(':
                l +=1
            elif c==')':
                r+=1
            if r>l:
                deletes.append(i+1)
                r -=1

        print(deletes)


        deleteLeft = self.delectLeft(s[deletes[-1]:], l-r)

        res = defaultdict(list)
        res[0,0] = ['']

        for i in range(1, len(deletes)): # deletes[i] is the end.
            for j in range(1, len(deletes)): # the number should be deleted
                curStr = s[deletes[i-1]: deletes[i]]
                res[deletes[i], j].extend([head+rear for head in res[deletes[i-1], j-1] for rear in self.delect(curStr)])

                res[deletes[i], j].extend([head+curStr for head in res[deletes[i-1], j]])
        return [head+rear for head in res[deletes[-1], len(deletes)-1] for rear in deleteLeft]

    def delect(self, s):
        res = []
        last = ''
        for i in range(len(s)):
            if s[i] == ')':
                if last==')':
                    continue
                else:
                    res.append(s[:i]+s[i+1:])
            last = s[i]
        return res



    def delectLeft(self, s, k):
        if k==0:
            return [s]
        s = ''.join([')' if i == '(' else '(' if i==')' else i for i in reversed(s)])
        print(s)
        res = self.removeInvalidParentheses(s)
        return [''.join([')' if i == '(' else '(' if i==')' else i for i in reversed(s)]) for s in res]




# print(Solution().removeInvalidParentheses("()())()(("))
# print(['(())()', '()()()'])
# print(Solution().removeInvalidParentheses("()())()"))
# print(['(())()', '()()()'])
#
# print(Solution().removeInvalidParentheses("(a)())()"))
# print(['(a())()', '(a)()()'])
#
# print(Solution().removeInvalidParentheses(")("))
# print([''])
#
# print(Solution().removeInvalidParentheses("()(()"))
# print(['()()'])
#
# print(Solution().removeInvalidParentheses("((()"))
# print(['()'])

# print(Solution().removeInvalidParentheses("(r(()()("))
# print(["r()()","r(())","(r)()","(r())"])

print(Solution().removeInvalidParentheses("()())r)"))
