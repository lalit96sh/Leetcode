class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = collections.defaultdict(list)
        
        for x,y,c in times:
            graph[x-1].append((c,y-1))
        q = [(0,k-1)]
        vis = set()
        x = n
        while q:
            (cur_cost,node) = heapq.heappop(q)
            if node in vis:
                continue
            ans = cur_cost
            vis.add(node)
            x-=1
            for wj,nj in graph[node]:
                if nj not in vis:
                    heapq.heappush(q,(wj+cur_cost,nj))
                
                    
            
        # print(cost,x)
        return -1 if x!=0 else ans