# Recursive
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = list()
        def dfs(node):
            if not node:
                return
            output.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        print(output)
        return output

# Iterative 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return
        
        stack, output = list(), list()
        stack.append(root)
        
        while stack:
            curr_node = stack.pop()
            output.append(curr_node.val)
            
            if curr_node.right:
                stack.append(curr_node.right)
            
            if curr_node.left:
                stack.append(curr_node.left)
        
        print(output)
        return output