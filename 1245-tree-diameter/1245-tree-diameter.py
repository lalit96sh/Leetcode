class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        
        n = len(edges)
        
        mp = collections.defaultdict(list)
        
        for s,d in edges:
            mp[s].append(d)
            mp[d].append(s)
        
        def dfs(root,parent):
            child_max = 0
            second_max = 0
            dmax = 0
            for node in mp[root]:
                if node!=parent:
                    max_dia, max_depth = dfs(node,root)
                    dmax = max(dmax,max_dia)
                    if max_depth>child_max:
                        second_max = child_max
                        child_max = max_depth
                    elif max_depth > second_max:
                        second_max = max_depth
                    
                    
                    
            
            
            return  max(1+child_max+second_max, dmax), 1+child_max
        return dfs(0,None)[0]-1
        
        
                    
                    
        