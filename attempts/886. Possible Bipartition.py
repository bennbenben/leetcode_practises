class Solution:
    """
    create a graph map
    do a bfs from each unvisited node
    """
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        # create a graph map: (key,val) = (node_1, node_1's dislikes)
        graph_map = {}
        for i in range(1,n+1):
            graph_map[i] = set()
        for pair in dislikes:
            graph_map[pair[0]].add(pair[1])
            graph_map[pair[1]].add(pair[0])
        # print(graph_map)
        
        # bfs function
        def bfs(node):
            # initialize queue
            q = collections.deque()
            q.append(node)
            
            while q:
                cur_node = q.popleft()
                
                for dislike_node in graph_map[cur_node]:
                    # check if person1 and dislike1 are in different groups
                    if (cur_node in group1 and dislike_node in group2) or \
                    (cur_node in group2 and dislike_node in group1):
                        continue
                    
                    # check if person1 and dislike1 are in same group
                    if (cur_node in group1 and dislike_node in group1) or \
                    (cur_node in group2 and dislike_node in group2):
                        return False
                    
                    # if person1 is in group1, add dislike1 to group 2
                    if cur_node in group1:
                        group2.add(dislike_node)
                    
                    # if person1 is in group2, add dislike1 to group1
                    if cur_node in group2:
                        group1.add(dislike_node)
                        
                    # if person1 is not in group1 nor group2, then add person1 and dislike1 to different groups
                    if (cur_node not in group1) and (cur_node not in group2):
                        group1.add(cur_node)
                        group2.add(dislike_node)
                    
                    # continue with q
                    q.append(dislike_node)
                    
            return True 
        
        # driver code
        group1, group2 = set(), set()                
        for i in range(1, n+1):
            # check if node i is in either groups
            if i in group1 or i in group2:
                continue
            # node i is not in either group - run BFS on node i to populate both groups
            else:
                bfs_output = bfs(i)
                if not bfs_output:
                    return False
                
        return True