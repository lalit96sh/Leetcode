class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        
        m = len(board)
        n = len(board[0])
        ans = []
        
        trie = {}
        
        for word in words:
            cur = trie
            for letter in word:
                cur[letter] = cur.setdefault(letter,{})
                cur = cur[letter]
            cur["$"] = word
            
        def dfs(i,j,tr):
            letter = board[i][j]
            
            cur = tr[letter]
            
            end = cur.pop("$",None)
            if end:
                ans.append(end)
            
            board[i][j] = "#"
            
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                if 0<=i+dx<m and 0<=j+dy<n and board[i+dx][j+dy] in cur:
                    dfs(i+dx,j+dy,cur)
                
            
            board[i][j] = letter
            
            if not tr[letter]:
                del tr[letter]
                
        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    dfs(i,j,trie)
        
        return ans