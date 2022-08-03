class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        
#         h = []
        
#         from heapq import heappush,heappop
#         n = len(stations)
#         for i in range(1,n):
#             heappush(h,(-abs(stations[i]-stations[i-1]),abs(stations[i]-stations[i-1]),1))
        
        
#         while k>0:
            
#             neg_max,orig,parts = heappop(h)
            
#             parts+=1
            
#             heappush(h,(-(orig/parts),orig,parts))
            
#             k-=1
            
        
#         return -h[0][0]
        
        n = len(stations)  
        def possible(val):
            
            return sum([int((stations[i]-stations[i-1])/val) for i in range(1,n)])<=k
        
        l = 0
        r = 1e8
        
        while r-l>=1e-6:
            mid = (l+r)/2
            
            if possible(mid):
                r = mid
            else:
                l = mid
                
        return l
        
        