# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node):
            # recursive base case
            if not node:
                return
            
            # start recursion
            left = dfs(node.left)
            right = dfs(node.right)
            
            # append and return results
            new_root = TreeNode(node.val)
            new_root.left = right
            new_root.right = left
            return new_root
        
        return dfs(root)