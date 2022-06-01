"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        node_mapping={}

        def dfs(node):
            if node in node_mapping:
                return node_mapping[node]

            clone_node = Node(node.val)
            node_mapping[node] = clone_node

            for neighbour in node.neighbors:
                clone_node.neighbors.append(dfs(neighbour))

            return clone_node

        return dfs(node)
