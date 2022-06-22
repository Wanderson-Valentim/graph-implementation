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
        if vertex in self.adjacency_list.keys():
            return True
        
        return False

    def has_edge(self, vi, vj, w):
        has_vi = self.has_vertex(vi)
        has_vj = self.has_vertex(vj)
        has_vi_vj = False       
        
        if not has_vi:
            raise ExceptionVertexDoesNotExist
        
        elif not has_vj:
            raise ExceptionVertexDoesNotExist
        
        else:
            has_vertex_in_vi = vj in self.adjacency_list[vi].keys()
            
            if has_vertex_in_vi:
                has_vi_vj = True
        
        return has_vi_vj
    
    def add_edge(self, vi, vj, w):
        has_vi_vj = self.has_edge(vi, vj, w)
        added_vi_vj = False
        
        if not has_vi_vj:
            #Adiciona a aresta em edges
            self.edges.append([vi, vj, w])
            
            #Adiciona a aresta na lista de adjacencias
            self.adjacency_list[vi][vj] = w 
            
            #Adiciona a aresta na matriz de adjacencias
            i, j = int(vi[1]), int(vj[1])
            self.adjacency_matrix[i][j] = 1
            
            added_vi_vj = True
        
        return added_vi_vj
        
    def remove_vertex(self, vi, vj, w):
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
            i, j = int(vi[1]), int(vj[1])
            self.adjacency_matrix[i][j] = 0
            
            removed_vi_vj = True
        
        return removed_vi_vj