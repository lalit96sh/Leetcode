class Solution:
    def longestWord(self, words: List[str]) -> str:
        
        trie = {}
        def create_trie(word):
            cur = trie
            for w in word:
                cur = cur.setdefault(w,{})
            
            cur["$"] = word
            
        for word in words:
            create_trie(word)
        # print(trie)
            
        
        ans = ""
        
        def dfs_trie(cur_trie, check_letter=None):
            
            if check_letter and check_letter not in cur_trie:
                return
            
            val = cur_trie.pop("$",None)
            
            nonlocal ans
            if val and len(val)>len(ans):
                ans = val
            sorted_keys = sorted(cur_trie.keys())
            for key in sorted_keys:
                
                dfs_trie(cur_trie[key], "$")
        
        dfs_trie(trie)
        return ans
                
                
        
        
                
        