class Solution(object):

    def distanceK(self, root, target, K):

        def dfs(node, parent=None):
            if node:
                node.parent = parent
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root)

        q = collections.deque()
        q.append((target, 0))
        seen = {target.val}
        while q:
            if q[0][1] == K:
                return [node.val for node, d in q]

            node, level = q.popleft()
            for neighbour in [node.left, node.right, node.parent]:
                if neighbour and neighbour.val not in seen:
                    seen.add(neighbour.val)
                    q.append((neighbour, level + 1))

        return []

