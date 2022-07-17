class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        
        from heapq import heappop, heappush
        
        n1 = len(nums1)
        n2 = len(nums2)
        
        h = []
        for i in range(min(k,n1)):
            heappush(h,(nums1[i]+nums2[0],i,0))
            
        ans = []
        for _ in range(k):
            if not h:
                break
            sm,i,j = heappop(h)
            
            ans.append([nums1[i],nums2[j]])
            
            if j==n2-1:
                continue
                
            heappush(h,(nums1[i]+nums2[j+1],i,j+1))
            
            
            
            
            
        return ans
        
        