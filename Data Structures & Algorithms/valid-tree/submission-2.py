class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        '''
        1. no cycles
        2. all nodes are reachable from any other node
            *if the edges are undirected
        n = 6
        edges = 5
                1
            2       3
          4  6 
          
          
          
          5

        tree_dfs(node, parent):
            add node to visited
            go through neighbors
                if parent, just ignore, dont need to dfs on it
                if neighbor is visited, return False
                if not dfs(neighbor, node) return False
            return True

        if we count edges, the graph
        MUST have n-1 edges
            > n-1 = cycle
            < n-1 = disconnected
        
            if we traverse the graph
            beginning from each node
            we should be able to visit 
            all nodes
            if not all nodes in the
            visited set, return False
        

        '''
        if n == 1 and edges == []:
            return True

        if len(edges) != n-1:
            return False
        
        adj_list = defaultdict(list) # maps node_val : [neighbor1, n2, ...]

        for node_a, node_b in edges:
            adj_list[node_a].append(node_b)
            adj_list[node_b].append(node_a)
        
        visited = set()

        def tree_dfs(node, parent):
            visited.add(node)

            for neighbor in adj_list[node]:
                if neighbor != parent:
                    if neighbor in visited or not tree_dfs(neighbor, node):
                        return False
            
            return True
        
        start_node = list(adj_list.keys())[0]
        start_parent = float('-inf')

        if not tree_dfs(start_node, start_parent):
            return False
        
        return len(visited) == n


