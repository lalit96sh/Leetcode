class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        
        mp = {
            "0": "0",
            "1":"1",
            "6": "9",
            "8": "8",
            "9": "6"
        }
        
        i = 0
        j = len(num)-1
        
        while i<=j:
            if mp.get(num[i])!=num[j]:
                return False
            i+=1
            j-=1
        
        return True