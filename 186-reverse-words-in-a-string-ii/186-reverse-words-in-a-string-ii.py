class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        n = len(s)
        
        def rev(i=0,j=n-1):
            
            while i<j:
                s[i],s[j] = s[j],s[i]
                i+=1
                j-=1
                
        rev()
        
        i = 0
        j = 0
        while j<n:
            
            while j<n and s[j]!=" ":
                j+=1
                
            rev(i,j-1)
            j+=1
            i = j
               
        
        
        