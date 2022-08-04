# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            
            if not root:
                return True,0
            
            l_flag,left_height = dfs(root.left)
            
            if not l_flag:
                return False,-1
            
            r_flag,right_height = dfs(root.right)
            
            if not r_flag:
                return False,-1
            
            return abs(left_height-right_height)<=1, 1+max(left_height,right_height)
        
        return dfs(root)[0]
        