# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # 1. find two nodes by recursion 
        # 2. we can simultanesouly count the level for each
        cur = root 

        if cur.val < p.val and cur.val < q.val:
            return self.lowestCommonAncestor(cur.right, p, q)
        elif cur.val > p.val and cur.val > q.val:
            return self.lowestCommonAncestor(cur.left, p, q)
        else:
            return cur
        
            