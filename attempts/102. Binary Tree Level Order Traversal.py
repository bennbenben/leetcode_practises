# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = list()
        if not root:
            return output
        
        def helper(node, i):
            # start current level
            if len(output) == i:
                output.append([])
            
            # append current node value
            output[i].append(node.val)
            
            # process child nodes for next level
            if node.left:
                helper(node.left, i+1)
            if node.right:
                helper(node.right, i+1)
            
        helper(root,0)
        return output