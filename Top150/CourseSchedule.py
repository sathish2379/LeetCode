'''
207. Course Schedule
Medium

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
'''
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # Step 1: Graph Initialization
        graph = defaultdict(list)
        for dest, src in prerequisites:
            graph[src].append(dest)

        def dfs(node):
            if visited[node] == 1:  # Cycle detected
                return False
            if visited[node] == 2:  # Already processed
                return True
        
            # Mark the node as currently visiting
            visited[node] = 1
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            
            # Mark the node as completely processed
            visited[node] = 2
            return True
        
        # Step 3: Initialize the visited array
        visited = [0] * numCourses
    
        # Step 4: Perform DFS for each node
        for course in range(numCourses):
            if visited[course] == 0:  # If the course is unvisited
                if not dfs(course):
                    return False
    
        return True