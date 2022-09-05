# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            
            if not root:
                return 0,0,float("inf")
            
            belowl,cur_without_cameral,cur_with_cameral = dfs(root.left)
            belowr,cur_without_camerar,cur_with_camerar = dfs(root.right)
            
            below = cur_without_cameral+cur_without_camerar
            cur_without_camera = min( cur_with_cameral + min(cur_with_camerar,cur_without_camerar),
                                    cur_with_camerar + min(cur_with_cameral,cur_without_cameral))
            
            cur_with_camera = 1+min(belowl,cur_without_cameral,cur_with_cameral)+min(belowr,cur_without_camerar,cur_with_camerar)
            
            return below,cur_without_camera,cur_with_camera
        return min(dfs(root)[1:])
        
        
            