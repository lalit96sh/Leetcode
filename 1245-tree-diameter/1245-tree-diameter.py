class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        
        dia = {}
        n = len(edges)
        
        mp = collections.defaultdict(list)
        
        for s,d in edges:
            mp[s].append(d)
            mp[d].append(s)
        
        def dfs(root,parent):
            if root in dia:
                return dia[root]
            
            nodes = 1
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
                    
                    
                    
            
            
            dia[root] = max(1+child_max+second_max, dmax), 1+child_max
            return dia[root]
        ans = 0
        for i in range(n+1):
            if i not in dia:
                dfs(i,None)
                
        return max([i[0] for i in dia.values()]) - 1
        
        
                    
                    
        