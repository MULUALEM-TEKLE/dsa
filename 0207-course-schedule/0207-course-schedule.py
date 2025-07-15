'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1
-> numCourses size small
-> from 0 to numCourses-1, zero indexed

You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
-> prerequisites size medium
-> always in pair
-> directed graph

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
-> directed from zero to one
-> gotta build a directed graph using a dictionary , src---->dst -> done

Return true if you can finish all courses. Otherwise, return false.
-> detect if there is any cycle in the graph
-> detect using state
    -> states -unvisited -visited -visiting
    -> use array for state, len=numCourses --> done
    -> initialize everything as unvisited and mark them visiting once we start to process them --> done
    -> process using bfs or dfs??? --> used dfs
    -> while we are visiting starting from a certain node if we find another visiting node we return true --> done
    -> if we get a visited node we return true --> done

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
        courses = prerequisites
        adj = defaultdict(list)
        for course,pre in courses : 
            adj[course].append(pre)
        UNVISITED = 0
        VISITING = 1
        VISITED = 2

        state = [UNVISITED] * numCourses
        def process(n) : 
            if state[n] == VISITING : return False
            if state[n] == VISITED : return True 
            state[n] = VISITING

            for pre in adj[n] : 
                if not process(pre) : return False
            
            state[n] = VISITED
            return True 

        for i in range(numCourses) : 
            if not process(i) : return False
        return True

        print(adj)