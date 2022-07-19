class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        ######## dfs
        
        n = len(graph)
        vis = {}
        
        def dfs(node):
            if node in  vis:
                return vis[node]
            
            vis[node] = True
            
            
            for i in graph[node]:
                if dfs(i):
                    return True
            
            
            vis[node] = False
            return False
        
        return [i for i in range(n) if not dfs(i)]
        
        
        #######################
        n = len(graph)
        out = collections.defaultdict(list)
        outdegree = collections.defaultdict(int)
        ans = set()
        for s,children in enumerate(graph):
            for d in children:
                out[d].append(s)
                outdegree[s]+=1
            
        
        q = collections.deque()
        
        for i in range(n):
            if outdegree[i]==0:
                q.append(i)
        
        while q:
            node = q.popleft()
            ans.add(node)
            
            for parent in out[node]:
                outdegree[parent]-=1
                if outdegree[parent]==0:
                    q.append(parent)
        
         
        return [i for i in range(n) if i in ans]
        
        