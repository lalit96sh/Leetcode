# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        count = 0
        def f(root):
            if not root:
                return root
            
            left = f(root.left)
            right = f(root.right)
            
            if root.val==p.val or root.val==q.val:
                nonlocal count
                count+=1
                return root
            
            if left and right:
                return root
            
            return (left or right)
        
        return f(root)