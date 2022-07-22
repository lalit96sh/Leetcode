class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        seen = {}
        graph = collections.defaultdict(list)
        for x,y in edges:
            graph[x].append(y)
            
        def dfs(node):
            
            if node in seen:
                return seen[node]
            
            if not graph[node]:
                return False if node==destination else True
            
            seen[node] = True
            
            for adj in graph[node]:
                
                if dfs(adj):
                    return True
                
            
            seen[node] = False
            return False
            
        return not dfs(source)