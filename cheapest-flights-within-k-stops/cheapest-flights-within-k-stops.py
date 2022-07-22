class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        graph = collections.defaultdict(list)
        vis = [float("inf")]*n
        for x,y,c in flights:
            graph[x].append((c,y))
        # print(graph)  
        from heapq import heappop,heappush
        
        pq = [(0,(src,k+1))]
        ans = float("inf")
        
        while pq:
            (cost,(node,stop_count)) = pq.pop(0)

            if node==dst:
                ans=min(ans,cost)
                continue
            if stop_count==0:
                continue
            for w,n_ in graph[node]:
                if vis[n_]<=cost+w:
                    continue
                else:
                    vis[n_] = cost+w
                    pq.append((cost+w,(n_,stop_count-1)))
        
        
        return ans if ans!=float("inf") else -1
#         if src == dst: return 0
#         d, seen = collections.defaultdict(list), collections.defaultdict(lambda: float('inf'))
#         for u, v, p in flights:
#             d[u] += [(v, p)]
    
#         q = [(src, -1, 0)]
        
#         while q:
#             pos, k, cost = q.pop(0)
#             if pos == dst or k == K: continue 
#             for nei, p in d[pos]:
#                 if cost + p >= seen[nei]:
#                     continue
#                 else:
#                     seen[nei] = cost+p
#                     q += [(nei, k+1, cost+p)]
                
#         return seen[dst] if seen[dst] < float('inf') else -1