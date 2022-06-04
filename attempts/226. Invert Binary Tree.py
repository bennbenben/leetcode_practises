# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root):
            # base case for recursion
            if not root:
                return
            
            # start recursion
            left = self.invertTree(root.left)
            right = self.invertTree(root.right)
            
            new_node = TreeNode(root.val)
            new_node.right = left
            new_node.left = right
            
            return new_node
        
        return dfs(root)
