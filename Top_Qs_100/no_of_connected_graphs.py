from collections import defaultdict


class Solution:
    def createGraph(self, edges):
        graph = defaultdict(list)

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        return graph

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = self.createGraph(edges)
        visited = set()
        count = 0

        for i in range(n):
            if i not in visited:
                count += 1
                self.dfs(i, visited, graph)

        return count

    def dfs(self, edge, visited, graph):

        if edge not in visited:
            visited.add(edge)
            for e in graph[edge]:
                self.dfs(e, visited, graph)