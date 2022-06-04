class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList or not beginWord or not endWord or not wordList:
            return 0
        
        n = len(beginWord)
        
        mp = collections.defaultdict(list)
        visited = set()
        
        for word in wordList:
            for i in range(n):
                inword = word[:i]+"*"+word[i+1:]
                mp[inword].append(word)
        
        
        q = [(beginWord,1)]
        visited.add(beginWord)
        
        while q:
            w,level = q.pop(0)
            for i in range(n):
                iword = w[:i]+"*"+w[i+1:]
                for word in mp[iword]:
                    if word==endWord:
                        return level+1
                    if word not in visited:
                        q.append((word,level+1))
                        visited.add(word)
                mp[iword]=[]
        return 0
                    
        