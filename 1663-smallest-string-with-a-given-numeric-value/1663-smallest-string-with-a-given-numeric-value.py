class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        
        ans = ""
        for i in range(n):
            
            if k-1<= (26*(n-i-1)):
                val = 1
            else:
                val = k-26*(n-i-1)
                
            k-=val
            ans+= chr(ord("a")+val-1)
        return ans
            
        
        