# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isMirrorImage(self, left, right):
        if left == None and right == None:
            return True
        if left == None or right == None:
            return False
        
        if left.val == right.val:
            outPair = self.isMirrorImage(left.left, right.right)
            innerPair = self.isMirrorImage(left.right, right.left)
            return outPair and innerPair
        else:
            return False
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        else:
            return self.isMirrorImage(root.left, root.right)