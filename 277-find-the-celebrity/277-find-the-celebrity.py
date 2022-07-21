# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        v = [0,1]
        
        next = 2
        while True:
            x = v[0]
            y = v[1]
            if knows(x,y)==True:
                v.remove(x)
            else:
                v.remove(y)
            
            if next==n:
                break
            v.append(next)    
            next+=1
        
        celebrity = v[0]
        
        for i in range(n):
            if i!=celebrity and (knows(i,celebrity)==0 or knows(celebrity,i)==1):
                return -1
            
                    
                    
        return celebrity
                    
             
                    