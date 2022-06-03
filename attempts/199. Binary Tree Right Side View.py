# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        DFS-traverse the tree right-to-left, add values to the view 
        whenever we first reach a new record depth. This is O(n).
        """
        output = list()
        
        def helper(node, i):
            # base case to return
            if not node:
                return
            
            # each level will only have one
            # start node val for each level
            if len(output) == i:
                output.append(node.val)
            
            # recursive calls
            if node.right:
                helper(node.right, i+1)
            if node.left:
                helper(node.left, i+1)
        
        helper(root,0)
        return output