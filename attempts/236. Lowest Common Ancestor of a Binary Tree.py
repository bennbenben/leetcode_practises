# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lowestCommon(root):
            # recursive base case - reject
            if not root:
                return None
            # recursive base case - accept
            if root == p or root == q:
                return root
            
            # start recursion
            left = lowestCommon(root.left)
            right = lowestCommon(root.right)
            
            # case 1 - both on same level
            if left and right:
                return root
            
            # case 2 - both not on same level
            if left:
                return left
            if right:
                return right
        
        return lowestCommon(root)
