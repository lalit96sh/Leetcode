class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        '''
        root
        
        f  
        
        l
        
        o i
        
        
        
        '''
        END_OF_CHARACTER = "$"
        trie = {}
        
        for word in strs:
            cur = trie
            
            for letter in word:
                cur[letter] = cur.setdefault(letter,{})
                cur = cur[letter]
                
            cur[END_OF_CHARACTER] = word
            
        
        ans = ""
        
        cur = trie
        # print(trie)
        while cur:
            if len(cur.keys())>1 or END_OF_CHARACTER in cur:
                return ans
            
            first_letter = list(cur.keys())[0]
            
            ans+=first_letter
            
            cur = cur[first_letter]
            
            
        
        
        return ans
                
                
        