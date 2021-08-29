class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [(root, False, 1)]
        maxHeight = 1
        while stack:
            node, visited, height = stack.pop()
            if visited:
                maxHeight = max(maxHeight, height)
            else:
                if node:
                    if node.left:
                        stack.append((node.left, False, height + 1))

                    stack.append((node, True, height))
                    if node.right:
                        stack.append((node.right, False, height + 1))
        return maxHeight

#         def maxDep(root, height):
#             if not root:
#                 return height - 1

#             left = maxDep(root.left, height + 1)
#             right = maxDep(root.right, height + 1)


#             return max(left, right)

#         return maxDep(root, 1)
