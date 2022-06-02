class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        
        l = None
        mx = 0
        for i,s in enumerate(seats):
            if s==1:
                print(mx,i,l)
                if l==None:
                    mx = i
                else:
                    mx = max(mx,(i-l)//2)
                l = i
        
        if l!=len(seats)-1:
            mx = max(mx,len(seats)-1-l)
        return mx