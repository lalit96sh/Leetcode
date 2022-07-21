class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        
        m = len(board)
        n = len(board[0])
        
        def dfs(i,j):
            
            board[i][j] = "B"
            
            adjs = [(i+dx,j+dy) for dx,dy in [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)] if 0<=i+dx<m and 0<=j+dy<n ]

            mine_count = 0
            
            next_adjs = []
            
            for x,y in adjs:
                if board[x][y]=="M":
                    mine_count+=1
                elif board[x][y]=="E":
                    next_adjs.append((x,y))
            # print(i,j)
            # print(next_adjs)
            if mine_count:
                board[i][j] = str(mine_count)
                return
            
            for x,y in next_adjs:
                dfs(x,y)
        
        x,y = click
        if board[x][y]=="M":
            board[x][y]="X"
            return board
        
        dfs(x,y)
        return board