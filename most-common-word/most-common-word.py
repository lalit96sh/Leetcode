class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        banned = set(banned)
        mp = collections.defaultdict(int)
        buff = []
        ans = ""
        
        
        for i,ch in enumerate(paragraph):
            
            if ch.isalnum():
                buff.append(ch.lower())
                if i != len(paragraph)-1:
                    continue
            
            if buff:
                word = "".join(buff)
                mp[word]+=1
                
                if word not in banned and mp[word]>mp[ans]:
                    ans = word
                buff = []
        return ans
            