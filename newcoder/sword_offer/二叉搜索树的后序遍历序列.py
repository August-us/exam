# 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。假设输入的数组的任意两个数字都互不相同
# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        if not sequence:
            return False
        return self.verify(sequence,0,len(sequence)-1)

    def verify(self,sequence,beg,end):
        if beg>=end:
            return True
        for i in range(beg,end):
            if sequence[i]>sequence[end]:
                for j in range(i+1,end):
                    if sequence[j]<sequence[end]:
                        return False
                break
        return self.verify(sequence,beg,i-1) and self.verify(sequence,i,end-1)