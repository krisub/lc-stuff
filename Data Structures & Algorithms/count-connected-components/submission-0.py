class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        '''
        1. adjacency list: each node mapped to its neighbors
            for loop through n1, n2 in edges
        2. set of visited nodes
            if we dfs a node which is NOT in the set of
            visited nodes, then it begins a new connected
            component
        start a stack holding node 1 -- or a queue
        1 : [2]
        2 : [3]
        4 : [5]

        1 -- 2      7
        |    |
        4 -- 5

        3. counting connected components:
            for each node in adjacency list
                if that node has NOT been visited
                    add to visited list
                    dfs on it (no neighbors then nothing happens)
                increment count of connected components (store this count) 
        
        4. the dfs itself: while there's nodes in our stack
            for the neighbors of the nodes
                if the neighbor has NOT been visited
                    say its visited and add to our stack
        '''

        adj_list = defaultdict(list)  # maps node val : [neighbor1, neighbor2, ...]
        # undirected: node_a <--> node_b
        for node_a, node_b in edges:
            adj_list[node_a].append(node_b)
            adj_list[node_b].append(node_a)
        
        visited = set() # hashset 
        
        connected_components = 0
        for node in range(n):
            if node not in visited:
                visited.add(node)
                self.dfs(node, adj_list, visited)
                connected_components += 1
        
        return connected_components
    
    def dfs(self, node, adj_list, visited):
        stack = [node]

        while stack:
            curr_node = stack.pop()
            for neighbor in adj_list[curr_node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)

