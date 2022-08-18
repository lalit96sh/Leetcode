class Solution:
    def minAvailableDuration(self, slot1: List[List[int]], slot2: List[List[int]], duration: int) -> List[int]:
        
        
        i = 0
        j = 0
        
        slot1.sort()
        slot2.sort()
        
        n1 = len(slot1)
        n2 = len(slot2)
        
        
        while i<n1 and j<n2:
            st1,e1 = slot1[i]
            st2,e2 = slot2[j]
            st = max(st1,st2)
            e = min(e1,e2)
            
            if e-st>=duration:
                return [st,st+duration]
            
            if e1<e2:
                i+=1
            else:
                j+=1
        return []