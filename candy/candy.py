class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        vals = [1]*n
        
        for i in range(1,n):
            if ratings[i]>ratings[i-1]:
                vals[i] = vals[i-1]+1
        print(vals)
        for j in range(n-2,-1,-1):
            if ratings[j]>ratings[j+1] and vals[j] <=vals[j+1]:
                vals[j] = vals[j+1]+1
        print(vals)
        return sum(vals)