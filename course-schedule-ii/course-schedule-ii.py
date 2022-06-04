class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        mp = collections.defaultdict(list)
        
        for c,p in prerequisites:
            mp[p].append(c)
        
        vis = {}
        r = []
        
        def dfs(course):
            if course in vis:
                return vis[course]
            
            vis[course]=True
            
            for pre in mp[course]:
                if dfs(pre):
                    return True
                
            r.append(course)
            vis[course]=False
            
        
        for course in range(numCourses):
            if dfs(course):
                return []
        return r[::-1]