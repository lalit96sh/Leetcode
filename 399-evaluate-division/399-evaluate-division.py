class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        group = {}
        
        def find(node):
            
            group_node,node_weight = group.setdefault(node,(node,1))
            
            if node!=group_node:
                new_group,new_weight = find(group_node)
                group[node] = (new_group,node_weight*new_weight)
                
            return group[node]
            
            
        def union(x,y,val):
            
            g_x,w_x = find(x)
            g_y,w_y = find(y)
            
            if g_x!=w_x:
                
                group[g_x] = (g_y, val*w_y/w_x )
                
        
        for (x,y),val in zip(equations,values):
            union(x,y,val)
            
        ans = []
        
        for x,y in queries:
            if x in group and y in group:
                g_x,w_x = find(x)
                g_y,w_y = find(y)
                if g_x!=g_y:
                    ans.append(-1.0)
                else:
                    ans.append(w_x/w_y)
            else:
                ans.append(-1.0)
        
        return ans