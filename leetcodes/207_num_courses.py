

class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        for x, y in prerequisites:
            graph[x].append(y)
        state = [0]*numCourses
        # state 0: have not been visited 
        # state 1: visted 
        # state -1: is being visited 

        def DFS(v): #have cyrcle? 
            if state[v] == 1:
                return False
            if state[v] == -1:
                return True
            
            state[v] = -1
            
            for node in graph[v]:
                if DFS(node):
                    return True
            
            state[v] = 1
            return False 
        
        for node in range(numCourses): #Can Finish?
            if DFS(node):
                return False
        return True

if __name__ == "__main__":

    obj = Solution()
    print(obj.canFinish(4, [[1,0], [0,1], [3, 1], [3, 2], [3, 0]]))
                