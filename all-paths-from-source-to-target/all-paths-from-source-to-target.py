class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        
        q = [(0,[])]
        ans = []
        vis = set()
        n = len(graph)
        while q:
            node,cur = q.pop()
            if node in vis:
                continue
            
            if node==n-1:
                ans.append(list(cur+[node]))
            else:
                for nx in graph[node]:
                    if nx not in vis:
                        q.append((nx,cur+[node]))
        return ans
#         n = len(graph)
#         vis = set()
#         ans = []
#         def dfs(node,cur):
#             if node == n-1:
#                 ans.append(list(cur+[node]))
#                 return
#             if node in vis:
#                 return
#             vis.add(node)
#             for next in graph[node]:
#                 if next not in vis:
#                     dfs(next,cur+[node])
#             vis.remove(node)
        
#         dfs(0,[])
#         return ans   
                
                
                
                
                
                
                
                
                
                
            