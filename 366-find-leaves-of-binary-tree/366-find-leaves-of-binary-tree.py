# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        mp = collections.defaultdict(list)
        
        def dfs(node):
            
            if not node:
                return 0
            
            l = dfs(node.left)
            r = dfs(node.right)
            
            node_level = 1+max(l,r)
            mp[node_level].append(node.val)
            
            return node_level
        
        last_level = dfs(root)
        
        return [mp[level] for level in range(1,last_level+1)]
        
        