class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        neg = 0
        if x<0:
            neg = 1
            x*=-1
        while x:
            x,md = divmod(x,10)
            ans = 10*ans + md
            if ans>2**31+neg-1:
                return 0
        return ans if not neg else -1 * ans
            
            
        