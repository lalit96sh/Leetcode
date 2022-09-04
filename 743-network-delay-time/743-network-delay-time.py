class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = collections.defaultdict(list)
        
        for x,y,c in times:
            graph[x-1].append((c,y-1))
        q = [(0,k-1)]
        vis = [float("inf")]*n
        vis[k-1] = 0
        # print(graph)
        while q:
            (cur_cost,node) = heapq.heappop(q)
            
            if cur_cost>vis[node]:
                continue
            for wj,nj in graph[node]:
                if vis[nj]>vis[node]+wj:
                    vis[nj] = vis[node]+wj
                    heapq.heappush(q,(vis[nj],nj))
                
        # print(vis)            
        ans = max(vis)    

        return -1 if ans==float("inf") else ans