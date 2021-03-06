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
    
    
    #Questão 3 - item c - EVertice(G, v): Verifica se v ∈ V (G) ou não.
    def has_vertex(self, vertex):
        return vertex in self.adjacency_list.keys()


    '''Questão 3 - item f - ExisteAresta(G, vi, vj , ω): Verifica se existe uma aresta 
    em G entre os vértices vi e vj com peso ω.'''
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
    
    
    '''Questão 3 - letra d - AddAresta(G, vi, vj , ω): Adiciona uma aresta em 
    G entre os vértices vi e vj com peso ω. Deve verificar se vi, vj ∈ V (G), 
    caso contrário a operação não poderá ser efetuada.'''
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


    '''Questão 3 - letra e - RemoveAresta(G, vi, vj , ω): Remove uma aresta em G 
    entre os vértices vi e vj com peso ω. Deve verificar se vi, vj ∈ V (G) e se 
    existe uma tal aresta, caso contrário a operação não poderá ser efetuada.'''
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
    
    
    #Questão 3 - item o - EAdj(G, vi, vj ): Verifica se vivj ∈ E(G).
    def check_if_is_adjacent(self, vi, vj):
        has_vi = self.has_vertex(vi)
        has_vj = self.has_vertex(vj)

        if not has_vi or not has_vj:
            raise ExceptionVertexDoesNotExist
        
        is_adjacent = vj in self.adjacency_list[vi].keys()
        
        return is_adjacent  
    
    
    '''Questão 3 - letra g - MudaPeso(G, vi, vj , ω, ω′): Modifica valor de peso de uma 
    aresta em G entre os vértices vi e vj de valor ω para o valor ω′. Deve verificar se 
    vi, vj ∈ V (G) e se existe uma tal aresta, caso contrário a operação não poderá ser 
    efetuada;'''
    def change_edge_weight(self, vi, vj, old_w, new_w):
        has_edge = self.has_edge(vi, vj, old_w)
        
        has_been_changed = False
        
        if has_edge:
            edge = [vi, vj, old_w]
            index = self.edges.index(edge)
            self.edges[index] = [vi, vj, new_w]
            
            self.adjacency_list[vi][vj] = new_w
            
            i, j = int(vi.replace('v','')) - 1, int(vj.replace('v','')) - 1
            self.weight_matrix[i][j] = new_w
        
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
        
        
    #Questão 3 - item k - GrafoSimples(G): Retorna se o grafo G é um grafo simples ou não.
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


    '''Questão 3 - item q - Incidencia(G, v): Devolve as arestas incidentes a v em G. Deve verificar se v ∈ V (G), caso contrário a operação não poderá ser efetuada.'''
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
            vertices.append([vj, vertex])
        
        return vertices
    
    
    '''Questão 3 - letra j - RecuperaPeso(G, vi, vj ): Devolve a lista de pesos de todas 
    as arestas entre os vértices vi e vj em V (G). Deve verificar se vi, vj ∈ V (G), 
    caso contrário a operação não poderá ser efetuada;'''
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


    #Questão 5 - Caminhos mínimos
    def bellman_ford(self, vertex):
        search_tree = [f'v{i+1}' for i in range(self.n)]

        costs = [[math.inf for _ in range(self.n)]
                    for _ in range(self.n+1)]
        
        index_vertex = int(vertex.replace('v',''))-1
        costs[0][index_vertex] = 0
        
        for l in range(1, self.n+1):
            for i in range(self.n):
                w1 = costs[l-1][i]
                w2 = math.inf
                
                vertices = self.incidence(f'v{i+1}')
                for vertex in vertices:
                    j = int(vertex[0].replace('v','')) - 1
                    w3 = costs[l-1][j] + self.weight_matrix[j][i]
                    if w3 < w2:
                        vertex_changes = f'v{j+1}'
                        w2 = w3
                
                if w1 > w2:
                    costs[l][i] = w2
                    search_tree[i] = vertex_changes
                else:
                    costs[l][i] = w1
               
        for i in range(self.n):
            if costs[self.n-1][i] != costs[self.n-2][i]:
                raise ExceptionContainsNegativeCycle
            
        return [costs[self.n-1], search_tree]


    def get_bellman_ford_result(self, vertex, return_type):
        has_vi = self.has_vertex(vertex)

        if not has_vi:
            raise ExceptionVertexDoesNotExist
        
        result = self.bellman_ford(vertex)
        
        if return_type == 'costs':
            return result[0]
        elif return_type == 'shortest_paths':
            return result[1]
    
    
    #Questão 5 - item  c - CaminhoMinimo(G, v): Devolve os caminhos mínimos entre vi ∈ V (G) e todos os demais vértices de G.
    def get_shortest_paths(self, vertex):
        shortest_paths = self.get_bellman_ford_result(vertex, 'shortest_paths')
        index_vertex = int(vertex.replace('v','')) - 1
        vertex_paths = {}
        vertex_paths[vertex] = {}
        
        for i in range(self.n):
            if i != index_vertex:
                vj = f'v{i+1}'
                vertex_paths[vertex][vj] = self.get_shortest_path_between_vi_vj(vertex, vj, shortest_paths)
        
        return vertex_paths
    
    
    #Questão 5 - item b - CustoMinimo(G, v): Devolve os custos dos caminhos mínimos entre vi ∈ V (G) e todos os demais vérticesde G.
    def get_minimal_costs(self, vertex):
        return self.get_bellman_ford_result(vertex, 'costs')


    #Questão 5 - item a - CaminhoMinimo(G, vi, vj ): Devolve um caminho mínimo entre vi e vj no grafo G.
    def get_one_shortest_path(self, vi, vj):
        has_vi = self.has_vertex(vi)
        has_vj = self.has_vertex(vj)

        if not has_vi or not has_vj:
            raise ExceptionVertexDoesNotExist
        
        shortest_paths = self.get_bellman_ford_result(vi, 'shortest_paths')
        
        index = int(vj.replace('v','')) - 1
        if shortest_paths[index] == vj:
            raise ExceptionDoesNotHaveAPathFromViToVj 
        
        return self.get_shortest_path_between_vi_vj(vi, vj, shortest_paths)
        
        
    def get_shortest_path_between_vi_vj(self, vi, vj, shortest_paths):
        builds = True
        path_edges = []
        
        index = int(vj.replace('v','')) - 1
        if shortest_paths[index] == vj:
            return path_edges
        
        while builds:
            index_vertex = int(vj.replace('v','')) - 1
            aux_vj = vj
            vj = shortest_paths[index_vertex]
            
            if vj == vi:
                weight = self.adjacency_list[vj][aux_vj]
                path_edges.insert(0, [vj, aux_vj, weight])
                builds = False
            else:
                weight = self.adjacency_list[vj][aux_vj]
                path_edges.insert(0, [vj, aux_vj, weight])
        
        return path_edges
    
    
    '''Quaetão 3 - item n - Complemento(G): Retorna o grafo complementar G de G.'''
    def complement(self):
        data = self.check_if_it_has_a_complement()
        
        if not data['has_complement']:
            raise ExceptionGraphHasNoComplement
        
        if data['graph_type'] == 'simple':
            return self.__complement_simple_graph()
        else:
            return self.__complement_digrapf()
        
        
    def __complement_simple_graph(self):
        complement = self.createNodes(self.n)
        weight = self.edges[0][2]
        
        for vi in self.adjacency_list.keys():
            for j in range(self.n):
                vj = f'v{j+1}'
                if vi != vj:
                    vj_in_vi = vj in self.adjacency_list[vi].keys()
                    
                    if not vj_in_vi:
                        complement[vi][vj] = weight
                        
        return complement
    
    
    def __complement_digrapf(self):
        complement = self.createNodes(self.n)
        
        for vi in self.adjacency_list.keys():
            for j in range(self.n):
                vj = f'v{j+1}'
                if vi != vj:
                    vj_in_vi = vj in self.adjacency_list[vi].keys()
                    
                    if vj_in_vi:
                        complement[vj][vi] = self.adjacency_list[vi][vj]
        
        return complement
    
    
    def check_if_it_has_a_complement(self):
        '''Esse método verifica se pode ser feito o complemento do grafo.
        O complemento só pode ser feito se o grafo for simples e todos os 
        pesos forem iguais ou se existe apenas um arco nesse de vi para
        vj ou vj para vi'''
        if self.m == 0:
            raise ExceptionGraphHasNoComplement
        
        is_simple_graph = self.check_if_the_graph_is_simple()
        
        if is_simple_graph:
            return {
                'has_complement': self.__check_if_it_has_a_complement_simple_graph(),
                'graph_type': 'simple'
            }
        else:
            return {
                'has_complement': self.__check_if_it_has_a_complement_digraf(),
                'graph_type': 'digraph'
            }
    
    
    def __check_if_it_has_a_complement_simple_graph(self):
        is_first_iteration = True
        
        for vi in self.adjacency_list.keys():
            for vj in self.adjacency_list[vi].keys():
                if is_first_iteration:
                    weight = self.adjacency_list[vi][vj]
                    is_first_iteration = False
                    
                elif weight != self.adjacency_list[vi][vj]:
                    return False
                    
        return True
        
        
    def __check_if_it_has_a_complement_digraf(self):
        for vi in self.adjacency_list.keys():
            if not len(self.adjacency_list[vi].keys()):
                return False
            
            for j in range(self.n):
                vj = f'v{j+1}'
                if vi != vj:
                    vi_in_vj = vi in self.adjacency_list[vj].keys()
                    vj_in_vi = vj in self.adjacency_list[vi].keys()
                    
                    if (vi_in_vj and vj_in_vi) or (not vi_in_vj and not vj_in_vi):
                        return False
        
        return True



    def has_cycle(self, v, visited, parent = None):
        visited[v] = True

        for node in self.adjacency_list[v]:
            if visited[node] == False:
                if self.has_cycle(node, visited, v) == True:
                    return True
            elif node != parent:
                return True

        return False


    def is_connected(self):
        visited = {}
        for v in self.adjacency_list:
            visited[v] = False
        
        self.has_cycle('v1', visited)
        
        for node in self.adjacency_list:
            if visited[node] == False:
                return False
    
        return True


    def is_tree(self):
        visited = {}
        for v in self.adjacency_list:
            visited[v] = False
        
        if self.has_cycle('v1', visited) == True:
            return False
        
        if self.is_connected():
            return True
        
        return False
    

    def is_bipartite_util(self, colors, v1 = 'v1'):
        queue = []
        queue.append(v1)

        while queue:
            u = queue.pop()

            if u in self.adjacency_list[u]:
                return False
            
            for node in self.adjacency_list:
                if colors[node] == -1 and node in self.adjacency_list[u]:
                    colors[node] = 1 - colors[u]
                    queue.append(node)
                elif colors[node] == colors[u] and node in self.adjacency_list[u]:
                    return False
        
        return True


    def is_bipartite(self):
        colors = {}
        for v in self.adjacency_list:
            colors[v] = -1
        
        for v in self.adjacency_list:
            if colors[v] == -1:
                if not self.is_bipartite_util(colors, v):
                    return False
        return True
    
    '''Questão 3 - item p - Adjacencia(G, v): Devolve a lista de adjacência de v em G. 
    Deve verificar se v ∈ V (G), caso contrário a operação não poderá ser efetuada.'''
    def get_adjacency_list(self, vertex):
        has_vertex = self.has_vertex(vertex)

        if not has_vertex:
            raise ExceptionVertexDoesNotExist

        return self.adjacency_list[vertex]
