import math
import queue
from ..exceptions.exceptions import *
class Graph:
    def __init__(self, name: str, n: int = 1, m: int = 0, edges: list = []):
        self.name = name
        self.n = n
        self.m = m
        self.edges = edges
        self.adjacency_list = self.generate_adjacency_list(edges, n, m)
        self.generate_adjacency_matrix(edges, n, m)
    
    def createNodes(self, num_vertices: int):
        """Cria os nós de um grafo para um dado número de vértices(num_vertices)"""
        graph = {}
        
        for num in range(num_vertices):
            graph[f'v{num + 1}'] = {}
        
        return graph

    def generate_adjacency_list(self, edges: list, num_vertices: int, num_edges: int):
        """Cria uma lista de adjacência com os vertices e suas respectivas arestas(edges) """
        graph = self.createNodes(num_vertices)
        
        if num_vertices > 1 and num_edges > 0:
            for edge in edges:
                graph[edge[0]][edge[1]] = edge[2]
        
        return graph
    
    def generate_adjacency_matrix(self, edges: list, num_vertices: int, num_edges: int):
        adjacency_matrix = [[0 for _ in range(num_vertices)]
                            for _ in range(num_vertices)]
        
        weight_matrix = [[math.inf for _ in range(num_vertices)]
                            for _ in range(num_vertices)]
        
        if num_vertices > 1 and num_edges > 0:
            for edge in edges:
                vertex1 = edge[0]
                vertex2 = edge[1]
                vi = int(vertex1.replace('v','')) - 1 
                vj = int(vertex2.replace('v','')) - 1
                adjacency_matrix[vi][vj] = 1
                weight_matrix[vi][vj] = int(edge[2])

        self.weight_matrix = weight_matrix
        self.adjacency_matrix = adjacency_matrix
    
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
        self.generate_adjacency_matrix(self.edges, self.n, self.m)
    
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
            i, j = int(vi.replace('v','')) - 1, int(vj.replace('v','')) - 1
            self.adjacency_matrix[i][j] = 1
            self.weight_matrix[i][j] = w
            
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
            i, j = int(vi.replace('v','')) - 1, int(vj.replace('v','')) - 1
            self.adjacency_matrix[i][j] = 0
            self.weight_matrix[i][j] = math.inf
            
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
                
                index = int(neighbour.replace('v','')) - 1
                search_tree[index] = vertex
                
                mark[neighbour]['color'] = 'gray'
                self.visit(neighbour, search_tree, mark, stack)
        
        mark[vertex]['color'] = 'black'
        
    def check_if_the_graph_is_simple(self):
        for vi in self.adjacency_list.keys():
            for vj in self.adjacency_list[vi].keys():
                has_vi_in_vj = vi in self.adjacency_list[vj].keys()
                has_vj_in_vi = vj in self.adjacency_list[vi].keys()

                if has_vi_in_vj and has_vj_in_vi:
                    weight_vi_vj = self.adjacency_list[vi][vj]
                    weight_vj_vi = self.adjacency_list[vj][vi]
                    if  weight_vi_vj != weight_vj_vi:
                        return False
                else:
                    return False
        
        return True

    def incidence(self, vertex):
        has_vertex = self.has_vertex(vertex)

        if not has_vertex:
            raise ExceptionVertexDoesNotExist
        
        is_simple = self.check_if_the_graph_is_simple()
        
        if is_simple:
            vertices = self.incidence_simple_graph(vertex)
        else:
            vertices = self.incidence_digraph(vertex)
            
        return vertices
            
    def incidence_digraph(self, vertex):
        vertices = []
        
        for vi in self.adjacency_list.keys():
            if vi != vertex:
                for vj in self.adjacency_list[vi].keys():
                    if vj == vertex:
                        vertices.append([vi, vertex])
        
        return vertices
    
    def incidence_simple_graph(self, vertex):
        vertices = []
        
        for vj in self.adjacency_list[vertex].keys():
            vertices.append([vertex, vj])
        
        return vertices
    
    def regain_weight(self, vi, vj):
        search_tree = self.depth_first_search(vi)
        has_vj = self.has_vertex(vj)

        if not has_vj:
            raise ExceptionVertexDoesNotExist
        
        index = int(vj.replace('v','')) - 1
        if search_tree[index] == vj:
            raise ExceptionDoesNotHaveAPathFromViToVj
        
        edge_weight_list = []
        builds = True
        
        while builds:
            index_vertex = int(vj.replace('v','')) - 1
            aux_vj = vj
            vj = search_tree[index_vertex]
            
            if vj == vi:
                weight = self.adjacency_list[vj][aux_vj]
                edge_weight_list.insert(0, [vj, aux_vj, weight])
                builds = False
            else:
                weight = self.adjacency_list[vj][aux_vj]
                edge_weight_list.insert(0, [vj, aux_vj, weight])
        
        return edge_weight_list


    def breadth_first_search(self, vi:str = 'v1'):
        """Faz a busca em largura de um vertice, retornando a árvore de busca
        até o momento que o nó foi encontrado.
        """
        search_tree = {}
        vertices_queue = queue.Queue()
        visited_vertices = {}

        for v in self.adjacency_list:
            visited_vertices[v] = False

        visited_vertices['v1'] = True
        vertices_queue.put('v1')

        while not vertices_queue.empty():
            v = vertices_queue.get()
            search_tree[v] = []
            for w in self.adjacency_list[v]:
                if not visited_vertices[w]:
                    visited_vertices[w] = True
                    vertices_queue.put(w)
                    search_tree[v].append(w)
                    if w == vi:
                        return search_tree
        return search_tree
