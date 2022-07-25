class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        
        
        rank = {}
        mp = collections.defaultdict(list)
        
        ans = set()
        
        for s,d in connections:
            mn,mx = min(s,d),max(s,d)
            
            mp[s].append(d)
            mp[d].append(s)
            
            ans.add((mn,mx))
            
        
        def dfs(node,parent,r):
            if node in rank:
                return rank[node]
            
            rank[node] = r
            
            mn = float("inf")
            
            for nei in mp[node]:
                if nei==parent:
                    continue
                
                nei_rank = dfs(nei,node,r+1)
                
                if nei_rank<=r:
                    ans.remove((min(node,nei),max(node,nei)))
                mn = min(mn,nei_rank)
                    
            return mn
        
        dfs(0,None,1)
        
        return ans
                
                
        