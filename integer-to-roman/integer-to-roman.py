class Solution:
    def intToRoman(self, num: int) -> str:
        
        mp = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X", 
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000:"M"             
        }
        
        nums = sorted(mp.keys(),reverse=True)
        
        ans = ""
        for nm in nums:
            if num==0:
                break
            val,num = divmod(num,nm)
            ans += (mp[nm]*val)
                
        return ans
        
        