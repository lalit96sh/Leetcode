class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        
        graph = collections.defaultdict(list)
        from heapq import heappush,heappop

        for i,w in enumerate(wells):
            graph[0].append((w,i+1))
            
        for s,d,c in pipes:
            graph[s].append((c,d))
            graph[d].append((c,s))

        pq = graph[0]
        heapq.heapify(pq)
        vis = set()
        vis.add(0)
        ans = 0
        
        while pq and len(vis)<n+1:
            
            cost,dest = heappop(pq)
            
            if dest not in vis:
                vis.add(dest)
                ans += cost
                
                for n_c,neig in graph[dest]:
                    if neig not in vis:
                        heappush(pq,(n_c,neig))
    
                
        return ans if len(vis)==n+1 else -1