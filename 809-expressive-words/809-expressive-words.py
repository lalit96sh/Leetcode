class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        
        def is_last_of_third(i):
            if i>1 and s[i]==s[i-1]==s[i-2]:
                return True
            return False

        def is_second_of_third(i):
            if i>0 and i<len(s)-1 and s[i-1]==s[i]==s[i+1]:
                return True
            return False
        
        def f(word):
            j = 0
            for i,ss in enumerate(s):
                if j<len(word) and word[j]==ss:
                    j+=1
                else:
                    if not (is_last_of_third(i) or is_second_of_third(i)):
                        return False
            return j==len(word)
                    
        return sum([f(w) for w in words])
                        
                
            