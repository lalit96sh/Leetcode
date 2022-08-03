class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        
        def is_allowed(val):
            
            sm = 0
            count = 1
            for weight in weights:
                if sm+weight>val:
                    count+=1
                    sm = 0
                sm+=weight
            
            return count<=days
                    
            
        
        mn = max(weights)
        mx = sum(weights)
        
        
        while mn<mx:
            
            mid = (mn+mx)//2
            
            if is_allowed(mid):
                mx=mid
            else:
                mn = mid+1
        return mn