class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        dp = [0]*(n+1)
        
        for i in range(1,n+1):
            w,h = books[i-1]
            dp[i] = dp[i-1]+h

            for j in range(i-1,0,-1):
                wj,hj = books[j-1]
                if w+wj>shelfWidth:
                    break
                h = max(h,hj)  
                dp[i] = min(dp[i],dp[j-1]+h)
                w = w+wj
        
        return dp[n]
            
            
            
            
            
            
        