class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        
        mp = {}
        
        for c in range(26):
            mp[chr(c+ord("a"))]  = (c//5,c%5)
            
        
        def return_moves(s,d):
            
            r = mp[d][0]-mp[s][0] # "D" for positive
            r_char = "D" if r>0 else "U"
            
            c = mp[d][1]-mp[s][1] # "R" for positive 
            c_char = "R" if c>0 else "L"
            
            
            if d=="z":
                return c_char*abs(c) + r_char*abs(r) +"!"
            
            return r_char*abs(r) + c_char*abs(c) + "!"
        
        s = "a"
        ans = ""
        for d in target:
            
            ans += return_moves(s,d) 
            
            s = d
        
        return ans
            
                
                
                
                
            
        