class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x==0:
            return 0
        
        l,r = 1,x//2
        
        while l<r:
            
            mid = (l+r+1)//2
            
            if mid*mid>x:
                r = mid-1
            else:
                l = mid
                
        
        return l
                