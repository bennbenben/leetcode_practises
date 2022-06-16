class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
            
        self.result = 0
        
        def dfs(node):
            # important to remember in tree recursion that your base cases return valid responses that do not break your solution
            if not node: return []
            if node.left == None and node.right == None: return [1]
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            # At each node you are returned a list of it's leaf nodes and their current node to leaf distance. This information can be used in the following 2 ways - 
            # 1. Check if you already found some valid pairs of leaves whose LCA is this current node.
            for l in left:
                for r in right:
                    if l + r <= distance:
                        self.result += 1
            
            # 2. Now pass this information onto this current node's parent such that the parent can make similar pairs at the next height. 
            nodes = []
            for l in left:
                nodes.append(l+1)
            for r in right:
                nodes.append(r+1)
            # But before you pass the updated list of leaves, make sure to update their depth. 
            return nodes
        
        dfs(root)
        return self.result