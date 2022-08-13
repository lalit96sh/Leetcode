# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        preindex = 0
        n = len(preorder)
        
        def get_index(nums,start,end,val):
            
            for i in range(start,end+1):
                if nums[i]==val:
                    return i
        
        def create_tree(prs,pre,pos,poe):
            if prs>pre or pos>poe:
                return None
            root =  TreeNode(preorder[prs])
            
            
            if prs+1<=pre:
                post_index = get_index(postorder,pos,poe,preorder[prs+1])
                new_pre = None
                if post_index+1<=poe-1:
                    pre_index = get_index(preorder,prs,pre,postorder[poe-1])
                
                    new_pre = pre_index-1
                if new_pre is not None:
                    root.left = create_tree(prs+1,new_pre,pos,post_index)
                    root.right = create_tree(new_pre+1,pre,post_index+1,poe-1)
                else:
                    root.left = create_tree(prs+1,pre,pos,post_index)

            return root
            
            
        
        
        return create_tree(0,n-1,0,n-1)