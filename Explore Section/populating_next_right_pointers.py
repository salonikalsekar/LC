from collections import defaultdict


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        h = defaultdict(list)

        def traverse(n, level, h):

            if n:
                h[level].append(n)
                if n.left:
                    traverse(n.left, level + 1, h)
                if n.right:
                    traverse(n.right, level + 1, h)

        res = []
        traverse(root, 1, h)

        for k, v in h.items():
            for i in range(len(v)):
                if i == len(v) - 1:
                    v[i].next = None
                else:
                    v[i].next = v[i + 1]

        return root