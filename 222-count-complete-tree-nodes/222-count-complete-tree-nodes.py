# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        def depth(root):
            ans = 0
            while root:
                ans+=1
                root=root.left
            return ans
        
        def help(root):
            if not root:
                return 0
            
            l = depth(root.left)
            r = depth(root.right)
            
            if l==r:
                return (2**l)+help(root.right)
            return (2**r)+help(root.left)
                    
                
        return help(root)