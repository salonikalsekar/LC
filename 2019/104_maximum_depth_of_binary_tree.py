# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def maxDepth(self, root: TreeNode) -> int:
#         res = []
#         height = 1
#         final, height =  self.depth(root, height)
#         return height


#     def depth(self, curr, height):
#         if not curr:
#             return [], height-1

#         left_list, lheight = self.depth(curr.left, height+1)
#         right_list, rheight = self.depth(curr.right, height+1)

#         return left_list + [curr.val] + right_list, max(lheight, rheight)


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        res = []
        height = 1

        stack = [(root, False, height)]
        if not root:
            return 0
        maxHeight = height
        while stack:
            curr, visited, height = stack.pop()
            maxHeight = max(maxHeight, height)
            if curr:
                if visited:
                    res.append(curr)
                else:
                    stack.append((curr.right, False, height + 1))
                    stack.append((curr, True, height))
                    stack.append((curr.left, False, height + 1))

        return (maxHeight - 1)






