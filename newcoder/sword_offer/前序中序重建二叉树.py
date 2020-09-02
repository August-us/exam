from typing import List
from TestCase import TreeNode


class Solution:
    # 返回构造的TreeNode根节点
    def buildTree_withList(self, pre: List[int], inorder: List[int]) -> TreeNode:
        if not pre:
            return
        root=TreeNode(pre[0])
        ind=inorder.index(pre[0])
        root.left=self.buildTree(pre[1:ind+1],inorder[:ind])
        root.right=self.buildTree(pre[ind+1:],inorder[ind+1:])

        return root

    def buildTree(self, preorder, inorder):
        '''对中序建立一个字典，这样可以直接获得中序每一个元素的索引'''
        def helper(in_left=0, in_right=len(inorder)):
            if in_left == in_right:
                return None

            # pick up pre_idx element as a root
            nonlocal pre_idx
            root_val = preorder[pre_idx]
            root = TreeNode(root_val)

            # root splits inorder list
            # into left and right subtrees
            index = idx_map[root_val]

            # recursion
            pre_idx += 1
            # build left subtree
            root.left = helper(in_left, index)
            # build right subtree
            root.right = helper(index + 1, in_right)
            return root

        # start from first preorder element
        pre_idx = 0
        idx_map = {val: idx for idx, val in enumerate(inorder)}
        return helper()

    # 从后序和中序构建树
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        '''对中序建立一个字典，这样可以直接获得中序每一个元素的索引'''
        def helper(start,end):
            if start>end:return
            nonlocal post_idx
            root_val=postorder[post_idx]
            root=TreeNode(root_val)
            post_idx-=1
            idx=idx_map[root_val]
            root.right=helper(idx+1,end)
            root.left=helper(start,idx-1)
            return root

        post_idx=len(postorder)-1
        idx_map={c:i for i,c in enumerate(inorder)}
        return helper(0,len(postorder)-1)




print(Solution().buildTree([1,2,4,7,3,5,6,8],[4,7,2,1,5,3,8,6]))


def FindNumsAppearOnce(array):
    tmp = 0
    list1 = []
    list2 = []
    for i in array:
        tmp ^=  i
    index_ = bin(tmp).replace('0b', '')[::-1].index('1') # 找出异或结果为1的最低位
    for i in array:
        if i>>index_&1==1:
            list1.append(i)
        else:
            list2.append(i)
    tmp1 = 0
    tmp2 = 0
    for i in list1:
         tmp1 ^= i
    for i in list2:
        tmp2 ^= i
    return tmp1, tmp2