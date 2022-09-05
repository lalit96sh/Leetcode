# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        
        cur = root
        
        temp = None
        
        prev = None
        
        while cur:
            
            next = cur.left
            
            x = cur.right
            cur.left = temp
            cur.right = prev
            
            
            
            temp = x
            
            prev = cur
            cur = next
        return prev
            
            
        