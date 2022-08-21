class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        
        n = len(books)
        memo = {}
        def dfs(start,width_remaining,highest):
            if start==n:
                return 0
            if (start,width_remaining,highest) in memo:
                return memo[(start,width_remaining,highest)]
            w,h = books[start]
            mx_h = max(h,highest)
            mn =float("inf")
            if shelfWidth!=width_remaining:
                mn = min(mn,highest+dfs(start,shelfWidth,0))
            
            if width_remaining>=w:
                mn = min(mn,dfs(start+1,width_remaining-w,mx_h))
                


            memo[(start,width_remaining,highest)] = max(mn,mx_h)
            return memo[(start,width_remaining,highest)]
        
        return dfs(0,shelfWidth,0)
            
            
            
        