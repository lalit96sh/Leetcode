class Solution:
    def baseNeg2(self, n: int) -> str:
        
        sign = 1
        ans = ""
        while n:
            n,mod = divmod(n,-2)
            if mod<0:
                n+=(2-1)
                mod+=2
            ans = str(mod)+ans
        return ans or "0"