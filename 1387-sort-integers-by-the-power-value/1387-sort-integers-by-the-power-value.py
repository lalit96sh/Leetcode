class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        
        def power(x):
            
            count = 0
            while x!=1:
                if x%2:
                    x = (3*x)+1
                else:
                    x = x//2
                count+=1
            return count
        
        from heapq import heappush,heappop
        heap = []
        
        for cur in range(lo,hi+1):
            
            heappush(heap,(-power(cur),-cur))
            
            if len(heap)>k:
                heappop(heap)
        
        print(heap)
        return -heappop(heap)[1]