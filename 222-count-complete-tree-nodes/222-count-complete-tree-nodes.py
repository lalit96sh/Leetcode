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
        def node_present(last_level_index,d,root):
            print("checking for {}".format(last_level_index))
            left = 0
            right = 2**d-1
            for _ in range(d):
                mid = left+(right-left)//2
                print(last_level_index,mid)
                if last_level_index <= mid:
                    print("left")
                    root=root.left
                    right = mid
                else:
                    print("right")
                    root = root.right
                    left = mid+1
            return root is not None
        
        def help(root):
            if not root:
                return 0
            
            l = depth(root.left)
            
            left = 0
            right = 2**l-1
            while left<right:
                mid = left+(right-left+1)//2
                if node_present(mid,l,root):
                    left = mid
                else:
                    right=mid-1
            
            return 2**l-1+left+1
                    
                
        return help(root)