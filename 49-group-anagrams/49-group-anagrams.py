class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        mp = collections.defaultdict(list)
        for st in strs:
            val = "".join(sorted(st))
            mp[val].append(st)
        
        return mp.values()
        