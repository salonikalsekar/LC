# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        
        res = self.dfs(root, '0')
        return res
        
        
    def dfs(self, node, val):
        
        if not node.left and not node.right:
            return int(val + str(node.val), 2)
        l, r = 0, 0
        if node.left:
            l = self.dfs(node.left, val + str(node.val))
            
        if node.right:
            r = self.dfs(node.right, val + str(node.val))
            
        return l + r
            
        
        
        
        
        
        
        
        