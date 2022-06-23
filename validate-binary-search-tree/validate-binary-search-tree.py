# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def f(root,mn=None,mx=None):
            if not root:
                return True
            if mn is not None and root.val<=mn:
                return False
            if mx is not None and root.val>=mx:
                return False
            return f(root.left,mn,root.val) and f(root.right,root.val,mx)
        return f(root)