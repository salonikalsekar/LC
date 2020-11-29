# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        if not root:
            return []
        dictTemp = defaultdict(list)
        queue = []
        dictTemp[1] = [root.val]
        queue.append((root, 1))
        print(dictTemp)
        while queue:
            curr, level = queue.pop(0)
            if curr:
                children = [curr.left, curr.right]

                if any(children):
                    for i in children:
                        if i:
                            dictTemp[level + 1].append(i.val)
                            queue.append((i, level + 1))

        return dictTemp.values()