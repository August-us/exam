n = int(input())


tree = [0 for i in range(n+1)]
root_candiate = set(list(range(1,n+1)))
class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = None if left == -1 else left
        self.right = None if right == -1 else right


for i in range(n):
    id, weight, left, right = [int(i) for i in input().split(' ')]
    tree[id] = TreeNode(weight, left, right)
    if left!= -1:root_candiate.remove(left)
    if right!= -1: root_candiate.remove(right)


res = 0
def preOrder(root: TreeNode, cur=[]):
    global res
    if root.left:
        root.left = tree[root.left]
        new_cur = [i ^ root.left.val for i in cur] + [root.left.val]
        preOrder(root.left, new_cur)
        res = max(max(new_cur), res)
    if root.right:
        root.right = tree[root.right]
        new_cur = [i ^ root.right.val for i in cur] + [root.right.val]
        preOrder(root.right, new_cur)
        res = max(max(new_cur), res)
root = root_candiate.pop()
preOrder(tree[root])
print(res)







'''
5
1 1 2 3
2 4 -1 -1
3 2 -1 4
4 5 -1 5
5 3 -1 -1
'''