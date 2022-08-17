# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        
        def dfs(root):
            
            if not root:
                return 0,0
            l,ls = dfs(root.left)
            r,rs = dfs(root.right)

            if l==0 and r==0:
                return 1,root.val
            
            return 1+max(l,r),ls+(rs if r>1 else 0)
        
        _,ans = dfs(root)
        return ans if _>1 else 0
            
            