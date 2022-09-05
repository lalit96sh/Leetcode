# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        
        ans = (0,0,0)
        
        def dfs(root):
            
            if not root:
                return 0,False
            
            l,foundl = dfs(root.left)
            if foundl:
                return None,True
            
            r,foundr = dfs(root.right)
            
            if foundr:
                return None,True
            
            
            if root.val==x:
                nonlocal ans
                ans = (l,r,n-(l+r+1))
                return None,True
            
            return 1+l+r,False
        _,found = dfs(root)
        if found:
            l,r,t = ans
            
            return t>(l+r) or l>(t+r) or r>(t+l)
            
        return False
        
        
        