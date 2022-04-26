class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def f(n):
            
            if n==0:
                return 1
            half, is_odd = divmod(n,2)
            half_value = f(n//2)
            
            ans = half_value*half_value
            
            if is_odd:
                ans*=x
            
            return ans
        
        return f(n) if n>=0 else 1/f(-n)