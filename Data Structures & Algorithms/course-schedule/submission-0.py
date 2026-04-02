class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #Building dependency list
        g = defaultdict(list)
        courses =  prerequisites
        for a , b in courses:
            g[a].append(b)
        
        # defining states
        visited = 2
        visiting = 1
        unvisited = 0
        states = [unvisited] * numCourses

        def dfs(node):
            state = states[node]
            if state == visited:
                return True
            elif state == visiting:
                return False

            states[node] = visiting
            for pre in g[node]:
                if not dfs(pre):
                    return False
            states[node] = visited
            return True 
            

        #if our reccursive dfs doesnt work, return false immidiately
        for i in range(numCourses):
            #run dfs
            if not dfs(i) :
                return False
        
        return True




        