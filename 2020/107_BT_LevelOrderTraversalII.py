# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return []
        dictTemp = defaultdict(list)
        queue = []
        dictTemp[1] = [root.val]
        queue.append((root, 1))

        while queue:
            curr, level = queue.pop(0)
            if curr:
                children = [curr.left, curr.right]

                if any(children):
                    for i in children:
                        if i:
                            dictTemp[level + 1].append(i.val)
                            queue.append((i, level + 1))

        for i in sorted(dictTemp.items(), reverse=True):
            res.append(i[1])
        return res