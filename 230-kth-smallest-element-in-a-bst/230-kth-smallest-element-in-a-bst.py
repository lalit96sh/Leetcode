# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        st = []
        node = root
        while node or st:
            cur = node
            while cur:
                st.append(cur)
                cur = cur.left
            
            pnode = st.pop()
            k-=1
            if k==0:
                return pnode.val
            node = pnode.right
        return -1
        