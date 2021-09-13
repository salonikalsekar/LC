class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        n = isConnected

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
                    print(self.root)
                self.c -= 1

        l = len(n)
        lc = len(n[0])
        self.c = l
        self.root = [i for i in range(l)]
        self.rank = l * [1]
        for i in range(l):
            for j in range(lc):
                if n[i][j] == 1:
                    print(i, j)
                    union(i, j)

        return self.c

