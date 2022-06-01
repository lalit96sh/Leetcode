class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        
        m = len(board)
        n = len(board[0])
        r = []
        
        trie = {}
        for w in words:
            node = trie
            for letter in w:
                node = node.setdefault(letter,{})
            node['$'] = w
        
        def f(i,j,p):
            letter = board[i][j]
            cur = p[letter]
            
            word_match = cur.pop('$',None)
            if word_match:
                r.append(word_match)
            board[i][j]="#"
            for x,y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if not( 0<=x<m and 0<=y<n) or board[x][y] not in cur:
                    continue
                f(x,y,cur)
            board[i][j]=letter
            if not cur:
                del p[letter]
        
        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    f(i,j,trie)
        return r