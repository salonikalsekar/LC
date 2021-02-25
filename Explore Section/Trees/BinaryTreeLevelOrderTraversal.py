# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict, deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return

        res = defaultdict(list)
        q = deque()

        q.append((root, 1))

        while q:
            curr, level = q.popleft()
            if curr:
                res[level].append(curr.val)
                q.append((curr.left, level + 1))
                q.append((curr.right, level + 1))

        return res.values()
