# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def isValid(node, left_value, right_value):
            if not node:
                return True
            if not (node.val > left_value and node.val < right_value):
                return False
            
            return (isValid(node.left, left_value, node.val) and 
            isValid(node.right, node.val, right_value))
        
        return isValid(root, -1*float("inf"), float("inf"))