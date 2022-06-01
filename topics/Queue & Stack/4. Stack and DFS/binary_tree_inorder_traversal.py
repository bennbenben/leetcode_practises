# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# this is the recursive technique
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # for in-order traversal, always go left, then root, then right
        if not root:
            return []
        return self.inorderTraversal(self.root.left) + [root.val] + 
        self.inorderTraversal(self.root.right)

# this is the iterative
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
