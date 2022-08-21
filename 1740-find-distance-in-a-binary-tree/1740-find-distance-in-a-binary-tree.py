# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        ans = None
        if p==q:
            return 0
        def lca(root):
            
            if not root:
                return 0,False,False
            
            
            lv,l_pflag,l_qflag = lca(root.left)
            if l_pflag and l_qflag:
                return lv,l_pflag,l_qflag
        
            rv,r_pflag,r_qflag = lca(root.right)
            if r_pflag and r_qflag:
                return rv,r_pflag,r_qflag
            
            pflag = l_pflag or r_pflag
            qflag = l_qflag or r_qflag
            
            val = 0
            
            if pflag:
                val+=1
            if qflag:
                val+=1
            
            return lv+rv+val, pflag or root.val==p , qflag or root.val==q
        
        return lca(root)[0]
            
            