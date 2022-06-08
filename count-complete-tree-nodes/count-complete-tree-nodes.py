# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = [root]
        cnt = 0
        while q:
            node = q.pop(0)
            cnt+=1
            for child in [node.left,node.right]:
                if not child:
                    return cnt+len(q)
                else:
                    q.append(child)
                    
                
        