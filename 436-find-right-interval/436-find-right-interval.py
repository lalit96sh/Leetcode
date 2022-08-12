class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        
        
        interval_index = [(s,e,idx) for idx,(s,e) in enumerate(intervals)]
        
        
        interval_index.sort()
        n = len(intervals)
        ans = [-1]*n
        
        def find_index(val):
            
            
            if interval_index[0][0]>val or interval_index[n-1][0]<val:
                return -1
            
            l = 0
            r = n-1
            while l < r:
                mid = (l+r)//2
                
                if interval_index[mid][0]<val:
                    l = mid+1
                else:
                    r = mid
            return interval_index[l][2]
        
        for s,e,idx in interval_index:
            
            ans[idx] = find_index(e)
            
        return ans
            
            
            