# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        # dest_flag = False
        # src_flag = False
        
        def lca(root):
            
            if not root:
                return "",False,False
            
            
            l,lsrc_flag,ldest_flag = lca(root.left)
            
            if lsrc_flag and ldest_flag:
                return l,True,True
            
            
            
            r,rsrc_flag,rdest_flag = lca(root.right)
            
            if rsrc_flag and rdest_flag:
                return r,True,True
            
            
            dest_flag = rdest_flag or ldest_flag
            src_flag = lsrc_flag or rsrc_flag
            
            
                
            if src_flag:
                st = l+"U" if lsrc_flag else r+"U"
            else:
                st = ""
                
            if dest_flag:
                st += ("L"+ l if ldest_flag else "R"+r)

                    
            return st, root.val==startValue or src_flag, root.val==destValue or dest_flag
            
        return lca(root)[0]
            
            
                
                
            
                
            
        