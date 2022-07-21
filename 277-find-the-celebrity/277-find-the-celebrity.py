# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        
        # celebrity_candidate = 0
        # for i in range(1, n):
        #     if self.cachedKnows(celebrity_candidate, i):
        #         celebrity_candidate = i
        
        celebrity = 0
        j=1
        while j < n:
            if knows(celebrity,j):
                celebrity = j
            j+=1
        
        for i in range(n):
            if i!=celebrity and (knows(i,celebrity)==0 or knows(celebrity,i)==1):
                return -1
            
                    
                    
        return celebrity
                    
             
                    