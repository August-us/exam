from typing import List

'''
给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。

示例:

输入: "25525511135"
输出: ["255.255.11.135", "255.255.111.35"]
'''
class Solution:
    def restoreIpAddresses_backtrack(self, s: str) -> List[str]:
        res=[]
        current=['']*4
        i=0
        k=0
        while k>=0 and i<len(s):
            if k==3:
                if s[i]!='0' or i==len(s)-1:
                    current[k] = s[i:]
                    if current[k] and int(current[k])<256:
                        res.append('.'.join(current))
                current[k]=''
                k-=1

            if current[k]!='0' and  int(current[k]+s[i])<256 and i<len(s)-1:
                current[k]+=s[i]

                i+=1
                k+=1
            else:
                i-=len(current[k])
                current[k]=''
                k-=1
        return res

    def restoreIpAddresses(self, s: str,last=2,start=0) -> List[str]:
        res=[]
        if start==len(s):return []
        if last==-1:
            if int(s[start:])<256 and  (s[start]!='0' or s[start:]=='0'):
                return [s[start:]]
            else:return []
        if s[start]=='0':return ['0.'+i for i in self.restoreIpAddresses(s,last-1,start+1)]
        for i in range(start+1,min(start+4,len(s)-last)):
            if int(s[start:i])>255:break
            res.extend([s[start:i]+'.'+back for back in self.restoreIpAddresses(s,last-1,i)])
        return res


print(Solution().restoreIpAddresses("010010"))




