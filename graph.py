from exceptions import *

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
        return vertex in self.adjacency_list.keys()

    def has_edge(self, vi, vj, w):
        has_vi = self.has_vertex(vi)
        has_vj = self.has_vertex(vj)     
        
        if not has_vi or not has_vj:
            raise ExceptionVertexDoesNotExist
        
        else:
            has_vertex_in_vi = self.check_if_is_adjacent(vi, vj)
            
            if has_vertex_in_vi:
                w_is_equal = w == self.adjacency_list[vi][vj]
                
                if w_is_equal:
                    return True
        
        return False
   
    def add_vertices(self, num_vertices):
        if num_vertices < 1:
            raise ExceptionInvalidOperation
        self.n += num_vertices
        self.adjacency_list = self.generate_adjacency_list(self.edges, self.n, self.m)
        self.adjacency_matrix = self.generate_adjacency_matrix(self.edges, self.n, self.m)
    
    def add_edge(self, vi, vj, w):
        has_vi = self.has_vertex(vi)
        has_vj = self.has_vertex(vj)
        has_vj_in_vi = self.check_if_is_adjacent(vi, vj)
        added_vi_vj = False

        if not has_vi or not has_vj:
            raise ExceptionVertexDoesNotExist
        
        if not has_vj_in_vi:
            #Adiciona a aresta em edges
            self.edges.append([vi, vj, w])
            
            #Adiciona a aresta na lista de adjacencias
            self.adjacency_list[vi][vj] = w 
            
            #Adiciona a aresta na matriz de adjacencias
            i, j = int(vi[1]) - 1, int(vj[1]) - 1
            self.adjacency_matrix[i][j] = 1
            
            self.m += 1
            
            added_vi_vj = True
        
        return added_vi_vj
        
    def remove_edge(self, vi, vj, w):
        has_vi_vj = self.has_edge(vi, vj, w)
        removed_vi_vj = False
        
        if has_vi_vj:
            #Remove a aresta de edges
            edge = [vi, vj, w]
            index = self.edges.index(edge)
            self.edges.pop(index)
            
            #Remove a aresta da lista de adjacencias
            self.adjacency_list.pop(vi)
            
            #Remove a aresta da matriz de adjacencias
            i, j = int(vi[1]) - 1, int(vj[1]) - 1
            self.adjacency_matrix[i][j] = 0
            
            self.m -= 1
            
            removed_vi_vj = True
        
        return removed_vi_vj
    
    def check_if_is_adjacent(self, vi, vj):
        has_vi = self.has_vertex(vi)
        has_vj = self.has_vertex(vj)

        if not has_vi or not has_vj:
            raise ExceptionVertexDoesNotExist
        
        is_adjacent = vj in self.adjacency_list[vi].keys()
        
        return is_adjacent  
    
    def change_edge_weight(self, vi, vj, old_w, new_w):
        has_edge = self.has_edge(vi, vj, old_w)
        
        has_been_changed = False
        
        if has_edge:
            edge = [vi, vj, old_w]
            index = self.edges.index(edge)
            self.edges[index] = [vi, vj, new_w]
            
            self.adjacency_list[vi][vj] = new_w
        
            has_been_changed = True
            
        return has_been_changed
    
    def depth_first_search(self, vertex):
        has_vertex = self.has_vertex(vertex)

        if not has_vertex:
            raise ExceptionVertexDoesNotExist
        
        stack = []
        search_tree = []
        mark = {}
        
        for i in range(self.n):
            mark[f'v{i+1}'] = {}
            mark[f'v{i+1}']['color'] = 'white'
            search_tree.append(f'v{i+1}')
            
        mark[vertex]['color'] = 'gray'
        
        self.visit(vertex, search_tree, mark, stack)
        
        return search_tree

    def visit(self, vertex, search_tree, mark, stack):
        stack.insert(0, vertex)
        for neighbour in self.adjacency_list[vertex]:
            if mark[neighbour]['color'] == 'white':
                
                index = int(neighbour.replace('v','')) - 1 if len(neighbour) > 2 else int(neighbour[1]) - 1
                search_tree[index] = vertex
                
                mark[neighbour]['color'] = 'gray'
                self.visit(neighbour, search_tree, mark, stack)
        
        stack.pop(0)
        mark[vertex]['color'] = 'black'