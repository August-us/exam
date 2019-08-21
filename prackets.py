alpha = ['1234567890']
def solu(s):
    ans = ""
    pattern = ""
    stack = []
    i = 0
    while i < len(s):
        if s[i] == '(':
            stack.append(i)
            i += 1
        elif s[i] == ')':
            f = stack.pop()
            pattern = solu(s[f+1:i])
            i += 1
        else:
            if len(stack) == 0:
                if s[i] in alpha:
                    j = i+1
                    while j < len(s) and s[j] in alpha:
                        j += 1
                    count = int(s[i:j])
                    ans += pattern*count
                    pattern = ""
                    i = j
                else:
                    if pattern != "":
                        ans += pattern
                        pattern = s[i]
                    else:
                        pattern = s[i]
                    i += 1
            else:
                i += 1

    ans += pattern
    return ans

c=int(input().strip())
for i in range(c):
    s =input().strip()
    print(solu(s))


'''
括号字符串识别，将数字k前的单位重复k次，单位可以是单独的字母，带括号的字符串
5
A11B
(AA)2A
((A2B)2)2G
(YUANFUDAO)2JIAYOU
A2BC4D2
'''
