class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # A topological sort can be used to check if there’s a cycle in the graph. The key idea is to:
        # - Process nodes with zero in-degree (courses that have no prerequisites).
        # - Remove edges as courses are "taken" (i.e., update in-degrees of other nodes).
        # - If you can process all nodes, it means there’s no cycle.

        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            # a, b = p[0], p[1]
            # b is a prerequisite of a
            graph[prereq].append(course)
            indegree[course] += 1

        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        count = 0
        while queue:
            course = queue.popleft()
            count += 1

            for course_next in graph[course]:
                indegree[course_next] -= 1
                if indegree[course_next] == 0:
                    queue.append(course_next)

        return count == numCourses
