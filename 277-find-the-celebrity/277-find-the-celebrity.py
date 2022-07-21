# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
     
    @lru_cache(maxsize=None)
    def cachedKnows(self, a, b):
        return knows(a, b)
    
    def findCelebrity(self, n: int) -> int:
        self.n = n
        celebrity_candidate = 0
        for i in range(1, n):
            if self.cachedKnows(celebrity_candidate, i):
                celebrity_candidate = i
        
        for i in range(n):
            if i!=celebrity_candidate and (knows(i,celebrity_candidate)==0 or knows(celebrity_candidate,i)==1):
                return -1
            
                    
                    
        return celebrity_candidate
                    
             
                    