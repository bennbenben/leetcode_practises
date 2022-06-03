# Recursive Solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = list()
        def postOrder(root):
            # base case to terminate tree traversal
            if not root:
                return
            # post order - left child -> right child -> root
            postOrder(root.left)
            postOrder(root.right)
            output.append(root.val)

        postOrder(root)
        return output

# Iterative Solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output, stack = list(), list()
        
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            temp = stack[-1].right
            if temp:
                root = temp
            else:
                temp = stack.pop()
                output.append(temp.val)
                while stack and stack[-1].right == temp:
                    temp = stack.pop()
                    output.append(temp.val)

        return output