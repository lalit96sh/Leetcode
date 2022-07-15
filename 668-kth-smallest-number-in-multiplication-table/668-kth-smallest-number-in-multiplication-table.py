class Solution:
    '''
    1,1         m,n
    '''
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        
        def enough(val):
            
            count = 0
            
            for i in range(1,m+1):
                if val<i:
                    break
                count+= min(val//i,n)
                
            return count>=k
        
        
        l = 1
        
        r = m*n
        
        while l<r:
            
            mid = (l+r)//2
            
            if not enough(mid):
                l = mid+1
            else:
                r=mid
                
        return l
        