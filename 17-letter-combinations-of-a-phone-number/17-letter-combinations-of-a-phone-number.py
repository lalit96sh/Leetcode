class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
               "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        
        def f(string,current,r):
            if not string:
                if current:
                    r.append(current)
                return
            first = string[0]
            
            for word in letters[first]:
                f(string[1:],current+word,r)
        r = []
        f(digits,"",r)
        return r
        
        