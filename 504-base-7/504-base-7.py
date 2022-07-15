class Solution:
    def convertToBase7(self, num: int) -> str:
        
        if num<0:
            return "-"+self.convertToBase7(-num)
        
        n, ans = num, ""
        
        while n:
            n, mod = divmod(n,7)
            
            ans = str(mod)+ans
        return ans or "0"
        