class Solution:
    def isHappy(self, n: int) -> bool:
        mp = set()
        mp.add(n)
        while n!=1:
            x = n
            sm = 0
            while x:
                sm+=((x%10)**2)
                x//=10
            n = sm
            if n in mp:
                break
            mp.add(n)
        return n==1
            