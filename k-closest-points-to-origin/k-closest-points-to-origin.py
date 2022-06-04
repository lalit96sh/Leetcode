class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def dis(p):
            return (p[0])**2 + (p[1])**2
        from heapq import heappush,heappop
        h = []
        for p in points:
            heappush(h,(dis(p),p))
        
        return [heappop(h)[1] for _ in range(k)]