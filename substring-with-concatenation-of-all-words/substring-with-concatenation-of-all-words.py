class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        mp = {}
        t_mp = {}
        
        wordlen = len(words[0])
        slen = len(s)
        for word in words:
            t_mp[word] = t_mp.get(word,0)+1
        word_count=len(words)
        cnt = 0
        i = 0
        result = []
        while i <=slen-wordlen:
            cur_word = s[i:i+wordlen]
            if cur_word in t_mp and mp.get(cur_word,0) < t_mp[cur_word]:
                mp[cur_word] = mp.get(cur_word,0) + 1
                cnt+=1
                i+=wordlen
                if cnt==word_count:
                    result.append(i-(cnt*wordlen))
                    i= i+1 - (cnt*wordlen)
                    mp = {}
                    cnt = 0
                    
            else:
                i= i+1- (cnt*wordlen)
                mp = {}
                cnt = 0
        return result
                
                
                
        