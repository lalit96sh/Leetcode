class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        mp = collections.defaultdict(list)
        
        for c,p in prerequisites:
            mp[p].append(c)
        
        vis = {}
        
        def dfs(course):
            if course in vis:
                return vis[course]
            
            vis[course]=True
            
            for pre in mp[course]:
                if dfs(pre):
                    return True
                
            
            vis[course]=False
            
        
        for course in range(numCourses):
            if dfs(course):
                return False
        return True
        