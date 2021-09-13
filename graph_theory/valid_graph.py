class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        def find(x):
            if x == self.root[x]:
                return x
            self.root[x] = find(self.root[x])
            return self.root[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if self.rank[rootX] < self.rank[rootY]:
                    self.root[rootX] = rootY
                elif self.rank[rootX] > self.rank[rootY]:
                    self.root[rootY] = rootX
                else:
                    self.root[rootY] = rootX
                    self.rank[rootX] += 1
                self.c -= 1
            else:
                return False

            return True

        if len(edges) != n - 1: return False
        self.c = 0
        self.root = [i for i in range(n)]
        self.rank = n * [1]
        for i in edges:
            if not union(i[0], i[1]):
                return False

        return True





