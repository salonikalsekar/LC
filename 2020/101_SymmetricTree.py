# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        if not root:
            return True

        queue = []
        tempDict = defaultdict(list)
        tempDict[1].append(root.val)
        queue.append((root, 1))

        while queue:

            curr, level = queue.pop(0)
            if curr:
                children = [curr.left, curr.right]
                for i in children:
                    if i:
                        tempDict[level + 1].append(i.val)
                    else:
                        tempDict[level + 1].append('null')
                    queue.append((i, level + 1))

        for k, v in tempDict.items():
            x = v[len(v) // 2:]
            if len(v) > 1:
                if v[:len(v) // 2] != x[::-1]:
                    return False
        return True