class GraphNode:
    def __init__(self):
        self.indegree = 0
        self.outNodes = []


from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = defaultdict(GraphNode)

        nodependencyCourses = []
        totalDep = 0
        for courses in prerequisites:
            prerequisiteCourse, nextCourse = courses[1], courses[0]

            g[prerequisiteCourse].outNodes.append(nextCourse)
            g[nextCourse].indegree += 1
            totalDep += 1

        removedEdge = 0
        for node, courses in g.items():
            if courses.indegree == 0:
                nodependencyCourses.append(node)

        while nodependencyCourses:

            currnode = nodependencyCourses.pop(0)

            for i in g[currnode].outNodes:
                g[i].indegree -= 1
                removedEdge += 1
                if g[i].indegree == 0:
                    nodependencyCourses.append(i)

        if removedEdge == totalDep:
            return True

        return False



