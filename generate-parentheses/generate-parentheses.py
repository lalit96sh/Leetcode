class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        ans = []
        
        def helper(l,r,cur):
            
            if r==0:
                ans.append(cur)
                return
            if l>0:
                helper(l-1,r,cur+"(")
            
            if l<r:
                helper(l,r-1,cur+")")
        
        helper(n,n,"")
        return ans
                