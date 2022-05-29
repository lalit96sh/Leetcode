class Solution:
    def trailingZeroes(self, n: int) -> int:
        
        x = 5
        c = 0
        while x<=n:
            c+=(n//x)
            x*=5
        return c
        