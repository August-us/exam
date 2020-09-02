def longestSubstringWithourDuplication(string):
    # 题目描述，请从字符串找出一个最长不包含重复字符的子串，统计该字符的长度。
    index={}
    curLength=0
    maxLength=0
    for i in range(len(string)):
        if string[i] not in index or (i-index[string[i]])>curLength:
            curLength+=1
        else:
            if curLength>maxLength:
                maxLength=curLength
            curLength=i-index[string[i]]
        index[string[i]]=i

    return max(maxLength,curLength)

print(longestSubstringWithourDuplication('arabcacfr'))