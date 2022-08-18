class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        ans = []
        n = len(num)
        i = 0
        while i<n:
            
            if (not ans) or ans[-1]<=num[i] or k==0:
                if num[i]!="0" or ans:
                    ans.append(num[i])
                
            else:
                while ans and ans[-1]>num[i] and k>0:
                    ans.pop()
                    k-=1
                if num[i]!="0" or ans: 
                    ans.append(num[i])

            i+=1
            
        if k!=0:
            while ans and k:
                ans.pop()
                k-=1
        
        return "".join(ans) if ans else "0"
        
        