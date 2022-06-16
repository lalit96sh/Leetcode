class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        n = len(s)
        mx = 1
        ans = s[0]
        for i in range(n):
            base = [(i,i+1),(i-1,i+1)]
            for left,right in base:
                while left>=0 and right<n and s[left]==s[right]:
                    if right-left+1>mx:
                        mx = right-left+1
                        ans = s[left:right+1]
                    
                    left-=1
                    right+=1
        
        return ans
                    
        