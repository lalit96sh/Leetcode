class Solution:
    def romanToInt(self, s: str) -> int:
        mp = {
            "I":       1,
            "V":       5,
            "X":       10,
            "L":       50,
            "C":       100,
            "D":       500,
            "M":       1000
        }
        last = 0
        ans = 0
        for st in s[::-1]:
            val = mp[st]
            if val<last:
                ans-=val
            else:
                ans+=val
                
            last = val
        return ans
                