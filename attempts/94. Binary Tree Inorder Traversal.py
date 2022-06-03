# Recursive solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = list()

        def inorder(root):
            # base case to terminate traversal
            if not root:
                return
            # inorder -> do left child, root, then right child
            inorder(root.left)
            output.append(root.val)
            inorder(root.right)

        inorder(root)
        return output

# Iterative Solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        tree_vals = []

        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            tree_vals.append(root.val)
            root = root.right
        return tree_vals