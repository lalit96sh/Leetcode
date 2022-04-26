class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        mp = collections.defaultdict(list)
        for st in strs:
            
            dp = [0]*26
            for letter in st:
                dp[ord(letter.lower())-ord('a')]+=1
            mp[tuple(dp)].append(st)
        
        return mp.values()
        