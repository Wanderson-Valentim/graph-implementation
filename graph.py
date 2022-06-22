class Graph:
    def __init__(self, name, n = 1, m = 0, edges = []):
        self.name = name
        self.n = n
        self.m = m
        self.edges = edges
        self.adjacency_list = self.generate_adjacency_list(edges, n, m)
        self.adjacency_matrix = self.generate_adjacency_matrix(edges, n, m)
    
    def createNodes(self, num_vertices):
        graph = {}
        
        for num in range(num_vertices):
            graph[f'v{num + 1}'] = {}
        
        return graph

    def generate_adjacency_list(self, edges, num_vertices, num_edges):
        graph = self.createNodes(num_vertices)
        
        if num_vertices > 1 and num_edges > 0:
            for edge in edges:
                graph[edge[0]][edge[1]] = edge[2]
        
        return graph
    
    def generate_adjacency_matrix(self, edges, num_vertices, num_edges):
        adjacency_matrix = [[0 for _ in range(num_vertices)]
                            for _ in range(num_vertices)]
        
        if num_vertices > 1 and num_edges > 0:
            for edge in edges:
                vertex1 = edge[0]
                vertex2 = edge[1]
                vi = int(vertex1[1]) - 1
                vj = int(vertex2[1]) - 1
                adjacency_matrix[vi][vj] = 1

        return adjacency_matrix
    
    def has_vertex(self, vertex):
        if vertex in self.adjacency_list.keys():
            return True
        
        return False

    def has_edge(self, vi, vj, w):
        has_vi = self.has_vertex(vi)
        has_vj = self.has_vertex(vj) 
        has_vi_vj = False       
        
        if has_vi and has_vj:
            has_vertex_in_vi = vj in self.adjacency_list[vi].keys()
            w_is_equal = w == int(self.adjacency_list[vi][vj])
            
            if has_vertex_in_vi and w_is_equal:
                has_vi_vj = True
        
        return has_vi_vj
    
    def add_edge(self, vi, vj, w):
        has_vi_vj = self.has_edge(vi, vj, w)
        
        if not has_vi_vj:
            self.adjacency_list[vi][vj] = w 
        
    def remove_vertex(self, vi, vj, w):
        has_vi_vj = self.has_edge(vi, vj, w)
        
        if has_vi_vj:
            self.adjacency_list.pop(vi)