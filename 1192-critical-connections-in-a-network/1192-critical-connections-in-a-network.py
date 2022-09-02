# class Solution:
#     def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        
        
#         rank = {}
#         mp = collections.defaultdict(list)
        
#         ans = set()
        
#         for s,d in connections:
#             mn,mx = min(s,d),max(s,d)
            
#             mp[s].append(d)
#             mp[d].append(s)
            
#             ans.add((mn,mx))
            
        
#         def dfs(node,parent,r):
#             if node in rank:
#                 return rank[node]
            
#             rank[node] = r
            
#             mn = float("inf")
            
#             for nei in mp[node]:
#                 if nei==parent:
#                     continue
                
#                 nei_rank = dfs(nei,node,r+1)
                
#                 if nei_rank<=r:
#                     ans.remove((min(node,nei),max(node,nei)))
#                 mn = min(mn,nei_rank)
#             print(node,mn)        
#             return mn
        
#         dfs(0,None,1)
        
        
        
#         return ans
                
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = set()
        seen = {}
        val = {}
        graph = collections.defaultdict(list)
        
        for x,y in connections:
            graph[x].append(y)
            graph[y].append(x)
            ans.add((min(x,y),max(x,y)))

        def dfs(node,value,parent):
            
            if node in val:
                return val[node]
            
            val[node] = value
            # seen.add(node)
            mn = value+1
            for child in graph[node]:
                if child!=parent:
                    child_val = dfs(child,value+1,node)
                    mn = min(mn,child_val)
                    if child_val<=value:
                        ans.discard((min(node,child),max(node,child) ))
            # seen.discard(node)
            
            return mn
            
        
        dfs(0,0,None)
        return ans    
    
        