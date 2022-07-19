class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
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
        
        