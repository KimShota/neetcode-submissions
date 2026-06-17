# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # we can go down the original tree until we find the subroot
        # if we dont find it, return False 
        # if we find it, check its left and right child until leaf nodes 
        # if there is mismatch, return False 
        # if they match, return True
        if not subRoot:
            return True 
        if not root:
            return False 

        if self.checkSubtree(root, subRoot):
            return True 
        
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))


    def checkSubtree(self, root, subRoot):
        if not root and not subRoot:
            return True 
        if root and subRoot and root.val == subRoot.val:
            return (self.checkSubtree(root.left, subRoot.left) and self.checkSubtree(root.right, subRoot.right))

        return False 
    
                
