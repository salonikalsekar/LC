class GraphNode:
    def __init__(self):
        self.indegree = 0
        self.outNodes = []


from collections import defaultdict


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = defaultdict(GraphNode)
        ordering = []
        nodependencyCourses = []
        totalDep = 0

        for courses in prerequisites:
            prerequisiteCourse, nextCourse = courses[1], courses[0]

            g[prerequisiteCourse].outNodes.append(nextCourse)
            g[nextCourse].indegree += 1
            totalDep += 1

        for node, courses in g.items():
            if courses.indegree == 0:
                nodependencyCourses.append(node)

        for i in range(numCourses):
            if i not in nodependencyCourses and g[i].indegree == 0:
                nodependencyCourses.append(i)

        while nodependencyCourses:

            currnode = nodependencyCourses.pop(0)
            ordering.append(currnode)
            for i in g[currnode].outNodes:
                g[i].indegree -= 1

                if g[i].indegree == 0:
                    nodependencyCourses.append(i)

        if len(ordering) == numCourses:
            return ordering

        return []
