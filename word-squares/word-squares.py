class Solution:
    def wordSquares(self, words):
        
        
        
        trie = {}
        def add_word_to_trie(word, tr):
            
            for letter in word:
                tr[letter] = tr.setdefault(letter,{})
                tr = tr[letter]
                if "#" not in tr:
                    tr["#"] = []
                tr["#"].append(word)
        
        def get_words_start_with_prefix(tr,prefix):

            for letter in prefix:
                if letter not in tr:
                    return []
                tr = tr[letter]
            
            return tr["#"]

        for word in words:
            add_word_to_trie(word,trie)
        
        ans = []
        n = len(words[0])
        def dfs(cur):
            step = len(cur)
            if step==n:
                ans.append(cur[:])
                return 
            
            prefix = "".join([x[step] for x in cur])
            
            next_words = get_words_start_with_prefix(trie,prefix)
        
            for w in next_words:
                dfs(cur+[w])
            
        
        for word in words:
            dfs([word])
            
        return ans
        