from collections import defaultdict


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        temp = defaultdict(list)
        if root:
            queue = [(root, 1)]

            while queue:

                n, level = queue.pop(0)
                temp[level].append(n.val)
                if n.left:
                    queue.append((n.left, level + 1))
                if n.right:
                    queue.append((n.right, level + 1))

        return temp.values()