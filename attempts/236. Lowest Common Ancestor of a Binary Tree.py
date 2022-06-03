# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def lowestCommon(root):
            # recursive base case (to stop recursion)
            if not root:
                return None
            # recursive base case (to stop recursion)
            if root == p or root == q:
                return root
            
            # start recursive
            left = lowestCommon(root.left)
            right = lowestCommon(root.right)
            
            # case 1 - both p and q found on same level
            if left and right:
                return root
            
            # case 2 - both found one different levels
            if left:
                return left
            else:
                return right

        return lowestCommon(root)