# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        #recursively retrieve the right and left side
        right = self.invertTree(root.right)
        left = self.invertTree(root.left)
        
        #initiatilize a new node
        newRoot = TreeNode(root.val)
        
        #assign mirror image to the new nodes
        newRoot.left = right
        newRoot.right = left
        
        #return the new node
        return newRoot