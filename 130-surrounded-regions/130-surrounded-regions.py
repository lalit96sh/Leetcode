class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        m = len(board)
        n = len(board[0])
        border = []
        for i in range(m):
            border.append([i,0])
            border.append([i,n-1])
        for i in range(1,n-1):
            border.append([0,i])
            border.append([m-1,i])
            
        def f(row,col):
            if not (0<=row<m and 0<=col<n):
                return
            if board[row][col]!="O":
                return
            board[row][col]="#"
            
            for i,j in [(0,-1),(0,1),(1,0),(-1,0)]:
                f(row+i,col+j)
        
        for b in border:
            f(b[0],b[1])
            
        for i in range(m):
            for j in range(n):
                if board[i][j]=="#":
                    board[i][j]="O"
                elif board[i][j]=="O":
                    board[i][j]="X"
            
        
        
        
        
