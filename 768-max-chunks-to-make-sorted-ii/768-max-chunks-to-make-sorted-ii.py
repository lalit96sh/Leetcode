class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        
        s = []
        
        for a in arr:
            mx = a
            while s and s[-1]>a:
                mx = max(mx,s.pop())
            
            s.append(mx)
        
        return len(s)
        