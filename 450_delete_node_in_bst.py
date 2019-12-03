# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.root = None

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        self.root = root
        self.delete_node(self.root, None, None, key)
        return self.root

    def min_right(self, curr):
        if curr.left == None:
            return curr
        else:
            return self.min_right(curr.left)

    def delete_node(self, curr, prev, is_left, key):
        if curr:
            if curr.val == key:
                if curr.left and curr.right:
                    minElement = self.min_right(curr.right)
                    curr.val = minElement.val
                    self.delete_node(curr.right, curr, False, minElement.val)

                elif curr.left == None and curr.right == None:
                    if prev:
                        if is_left:
                            prev.left = None
                        else:
                            prev.right = None
                    else:
                        self.root = None


                elif curr.left == None:
                    if prev:
                        if is_left:
                            prev.left = curr.right
                        else:
                            prev.right = curr.right
                    else:
                        self.root = curr.right
                else:
                    if prev:
                        if is_left:
                            prev.left = curr.left
                        else:
                            prev.right = curr.left
                    else:
                        self.root = curr.left

            elif key < curr.val:
                self.delete_node(curr.left, curr, True, key)

            elif key > curr.val:
                self.delete_node(curr.right, curr, False, key)


