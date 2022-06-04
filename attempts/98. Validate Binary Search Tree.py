# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def isValid(root, left_val, right_val):
            # base case to stop recursion
            if not root:
                return True
            if not (root.val > left_val and root.val < right_val):
                return False
            
            # start recursion
            left = isValid(root.left, left_val, root.val)
            right = isValid(root.right, root.val, right_val)
            
            # validate recursion result
            if left and right:
                return True
            else:
                return False
        
        return isValid(root, -1*float('inf'), float('inf'))
