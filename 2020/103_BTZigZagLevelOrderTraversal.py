# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:

        if not root:
            return []

        queue = []
        queue.append((root, 1))
        tempDict = defaultdict(list)
        tempDict[1].append(root.val)

        while queue:
            res = []
            curr, level = queue.pop(0)

            if curr:
                children = [curr.left, curr.right]
                if any(children):
                    for i in children:
                        if i:
                            tempDict[level + 1].append(i.val)
                            queue.append((i, level + 1))

        for k, v in tempDict.items():
            if k % 2 == 0:
                res.append(v[::-1])
            else:
                res.append(v)
        return res