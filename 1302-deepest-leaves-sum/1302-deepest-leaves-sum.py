# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        '''
        
        
        sum,level
        
        if both level equals:
        
        lsum+rightsum,level+1
        
        level1>levelright:
            left_sum,lefttlevel+1
            
            
            
        0,-1
        0,-1
        
        7,1
        
        
            
        
        '''
        
        def dfs(root):
            
            if not root:
                return 0,-1
            
            l_sum,l_level = dfs(root.left)
            r_sum,r_level = dfs(root.right)
            
            if l_level==-1 and r_level==-1:
                return root.val,1
            
            if l_level==r_level:
                return l_sum+r_sum,l_level+1
            
            if l_level>r_level:
                return l_sum,l_level+1
            return r_sum,r_level+1
        
        return dfs(root)[0]
            
            
        