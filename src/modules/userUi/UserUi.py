import os
import math
import platform
from ..exceptions.exceptions import *
from ..graph.Graph import Graph
from functions import *


class UserUI:
    def __init__(self):
        self.text_size = 70
        self.options = 'OPÇÕES'
        self.basic_operations = 'OPERAÇÕES  BÁSICAS'
        self.routes = 'PERCURSOS'
        self.shortest_path = 'CAMINNHOS  MÍNIMOS'
        self.graphs = 'IMPLEMENTAÇÃO GRAFOS'
        self.isMenuOpen = True


    def __print_menu_option(self, menu = 'graphs'):
        menu_text = getattr(self, menu)
        text_size = len(menu_text)
        dash_quantity = int((self.text_size - (text_size + 2)) / 2)
        dashes = '-' * dash_quantity
        clear_str = 'cls' if platform.system() == 'Windows' else 'clear'
        os.system(clear_str)
        print(f'\n{dashes}{menu_text}{dashes}\n')


    def __print_line(self):
        print('-' * (self.text_size - 2))


    def __print_text(self, text: str):
        size = int((self.text_size - len(text)) / 2)
        space = ' ' * size
        print(f'{space}{text}{space}\n')

    
    def __print_header(self, text: str, option = 'graphs'):
        self.__print_menu_option(option)
        self.__print_text(f'--> {text} <--')
        self.__print_line()
        
    
    def __print_path(self, path):
        total_cost = int(path[0][2])
        representation = f'\t    {path[0][0]} --({path[0][2]})--> {path[0][1]}'
        
        for i in range(1, len(path)):
            total_cost += int(path[i][2])
            representation += f' --({path[i][2]})--> {path[i][1]}'
        
        print(representation)
        print(f'\t    O custo total do caminho é {total_cost}.')


    def __print_some_paths(self, vertex_paths):
        vertex = list(vertex_paths.keys())[0]
        for vj in vertex_paths[vertex]:
            if len(vertex_paths[vertex][vj]) == 0:
                print(f'\t--> Não existe caminho mínimo entre {vertex} e {vj}.\n')
            else:
                print(f'\t--> O caminho mínimo entre {vertex} e {vj}.')
                self.__print_path(vertex_paths[vertex][vj])
                print()


    def __print_costs(self, vertex, costs):
        index_vertex = int(vertex.replace('v','')) - 1
        for i in range(len(costs)):
            if i != index_vertex:
                if costs[i] == math.inf:
                    print(f'\t--> O custo mínimo entre {vertex} e v{i+1} é infinito.\n')
                else:
                    print(f'\t--> O custo mínimo entre {vertex} e v{i+1} é {costs[i]}.\n')
                    

    #Questão 3 - item h - ImprimeGrafo(G): Imprime todos os vértices e arestas de G.
    def __print_graph(self, graph):
        is_first_iteration = True
        representation_graph, vertices, edges = '', '', ''
        
        for vi in graph.adjacency_list.keys():
            if is_first_iteration:
                vertices += f'{vi}'
                is_first_iteration = False
            else:
                vertices += f' - {vi}'
                
            for vj in graph.adjacency_list[vi].keys():
                edges += f'\t    {vi} --({graph.adjacency_list[vi][vj]})--> {vj}\n'
        
        representation_graph += f'\t--> Vértices do grafo {graph.name}:\n'
        representation_graph += '\t    ' + vertices + '\n\n'
        representation_graph += f'\t--> Arestas do grafo {graph.name}:\n'
        representation_graph += edges
        print(representation_graph)
    
    
    def __print_adjacency_lists(self, adjacency_list, vi):
        print(f'\t[{vi}] --> ', end='')
        for vertex in adjacency_list[vi]:
            print(f'[{vertex}] --> ', end='')
        print('λ')
    
    
    def __print_adjacency_list_vertex(self, adjacency_list, vi):
        print(f'\t[{vi}] --> ', end='')
        for vertex in adjacency_list:
            print(f'[{vertex}] --> ', end='')
        print('λ')


    #Questão 3 - item s - ImprimeMatrizAdj(G): Imprime a matriz de adjacência de G.
    def __print_adjacency_matrix(self, graph):
        for i in range(len(graph.adjacency_matrix)):
            print(f'\t    {graph.adjacency_matrix[i]}')
            
    
    def __print_matrix(self, matrix):
        for i in range(len(matrix)):
            print(f'\t    {matrix[i]}')


    def __graph_from_file(self, file_name):
        data = read_file(file_name)
        name = data['information'][0]
        n = int(data['information'][1])
        m = int(data['information'][2])
        edges = data['edges']
        save_graph(name, n, m, edges)
        graph = Graph(name, n, m, edges)
        self.__print_menu_option('options')
        self.__options_screen(graph)
    
    
    #Questão 3 - item a - NovoGrafo(): Retorna um grafo vazio, ou seja, com apenas um novo vértice.
    def __new_graph(self):
        name = input('\tEscolha o nome do Grafo: ')
        graph = Graph(name)
        save_graph(name)
        self.__print_menu_option('options')
        self.__options_screen(graph)
    

    def __saved_graph(self):
        saved = get_saved_graph()
        was_saved = saved['has_saved_graph']

        if was_saved:
            name = saved['graph']['name']
            n = int(saved['graph']['n'])
            m = int(saved['graph']['m'])
            edges = saved['graph']['edges']
            graph = Graph(name, n, m, edges)
            self.__print_menu_option('options')
            self.__options_screen(graph)
        else:
            self.__print_header('Não Possui Grafo Salvo!')
    
    #Questão 3 - item i - RemoveGrafo(G): Libera todo o espaço utilizado pela representação de G.
    def __remove_graph(self):
        remove_saved_graph()
        self.__print_header('Grafo Removido!')
    

    def __close(self):
        self.isMenuOpen = False


    def __home_screen(self):
        options = [
            ['Grafo a Partir de Um Arquivo', self.__graph_from_file],
            ['Novo Grafo', self.__new_graph],
            ['Grafo Salvo', self.__saved_graph],
            ['Remove Grafo', self.__remove_graph],
            ['Fechar', self.__close],
        ]

        for i in range(len(options)):
            print(f'\t--> {options[i][0]} ({i + 1})')

        try:
            home_screen_option = int(input('\tEscolha a Opção -> '))
            if not(home_screen_option in range(1, 6)):
                raise ExceptionInvalidOperation
            else:
                if home_screen_option == 1:
                    file_name = input('\tDigite o Nome do Arquivo -> ')
                    options[home_screen_option - 1][1](file_name)
                else:
                    options[home_screen_option - 1][1]()
        except FileNotFoundError:
            self.__print_header('Não existe arquivo com esse nome!')
        except:
            self.__print_header('Opção Inválida. Escolha Novamente!')


    def __open_option(self, graph, method = None, option = 'graphs'):
        self.__print_menu_option(option)
        if not(method is None):
            method(graph)
        else:
            return


    def __options_screen(self, graph):
        options = [
            ['Tela Anterior', lambda graph: self.__open_option(graph)],
            ['Operações Básicas', lambda graph: self.__open_option(graph, self.__basic_operations_screen, 'basic_operations')],
            ['Percursos', lambda graph: self.__open_option(graph, self.__route_screen, 'routes')],
            ['Caminhos Mínimos', lambda graph: self.__open_option(graph, self.__shortest_path_screen, 'shortest_path')],
        ]

        for i in range(len(options)):
            print(f'\t{options[i][0]} ({i})')
        
        try:
            option = int(input('\tEscolha a Opção -> '))
            
            if not(option in range(0, 4)):
                raise ExceptionInvalidOperation
            else:
                options[option][1](graph)
        except ExceptionInvalidOperation:
            self.__print_header('Opção Inválida. Escolha Novamente!', 'options')
            self.__options_screen(graph)
        except NameError:
            print(NameError)


    def __basic_operations_screen(self, graph: Graph):
        print('\tTela Anterior (0)')
        print('\tAdicionar Vértices (1)') #OK
        print('\tAdicionar Aresta (2)') #OK
        print('\tRemover Aresta (3)') #OK
        print('\tMudar Peso (4)') #OK
        print('\tRecupera Peso (5)')#OK
        print('\tIncidência (6)')#OK
        print('\tVerificar se Vértice Pertence ao Grafo (7)') #OK
        print('\tVerificar se Aresta Pertence ao Grafo (8)') #OK
        print('\tImprime Grafo (9)')
        print('\tImprime Matriz de Pesos (10)') #Ok
        print('\tImprime Matriz de Adjacências (11)') #OK
        print('\tImprime Lista de Adjacências (12)') #Ok
        print('\tImprime Lista de Adjacências de um Vértice (13)') #OK
        print('\tVerifica se é Vizinho (14)') #OK
        print('\tVerifica se Grafo é Simples (15)')#OK
        print('\tVerifica se Grafo é Conexo (16)')
        print('\tVerifica se Grafo é Bipartido (17)')
        print('\tVerifica se Grafo é Árvore (18)')
        print('\tComplemento do Grafo(19)\n')#OK

        try:
            choise = int(input('\tEscolha a Opção -> '))

            if choise == 0:
                self.__print_menu_option('options')
                self.__options_screen(graph)
                
            elif choise == 1:
                num_vertices = int(input('\tDigite a quantidade de vértices -> '))
                graph.add_vertices(num_vertices)
                save_graph(graph.name, graph.n, graph.m, graph.edges)
                self.__print_menu_option('basic_operations')
                self.__basic_operations_screen(graph)
                
            elif choise == 2:
                vi = input('\tDigite o vertice vi -> ')
                vj = input('\tDigite o vertice vj -> ')
                w = input('\tDigite o peso w -> ')
                self.__print_menu_option('basic_operations')
                
                added_edge = graph.add_edge(vi, vj, w)
                if added_edge:
                    save_graph(graph.name, graph.n, graph.m, graph.edges)
                    self.__basic_operations_screen(graph)
                else:
                    raise ExceptionCouldNotAddEdge
                
            elif choise == 3:
                vi = input('\tDigite o vertice vi -> ')
                vj = input('\tDigite o vertice vj -> ')
                w = input('\tDigite o peso w -> ')
                self.__print_menu_option('basic_operations')
                remove_edge = graph.remove_edge(vi, vj, w)
                if remove_edge:
                    save_graph(graph.name, graph.n, graph.m, graph.edges)
                    self.__basic_operations_screen(graph)
                else:
                    raise ExceptionUnableToRemoveEdge
            
            elif choise == 4:
                vi = input('\tDigite o vertice vi -> ')
                vj = input('\tDigite o vertice vj -> ')
                old_w = input('\tDigite o atual peso w -> ')
                new_w = input('\tDigite o novo peso w -> ')
                self.__print_menu_option('basic_operations')
                has_been_changed = graph.change_edge_weight(vi, vj, old_w, new_w)
                
                if has_been_changed:
                    save_graph(graph.name, graph.n, graph.m, graph.edges)
                    self.__basic_operations_screen(graph)
                else:
                    raise ExceptionEdgeDoesNotExist
                
            elif choise == 5:
                vi = input('\tDigite o vertice vi -> ')
                vj = input('\tDigite o vertice vj -> ')
                self.__print_menu_option('basic_operations')
                print(f'\t--> Pesos das arestas entre os vértices {vi} e {vj}')
                edge_weight_list = graph.regain_weight(vi, vj)
                
                for i in range(len(edge_weight_list)):
                    print(f'\t    {edge_weight_list[i][0]} ---> {edge_weight_list[i][1]} com peso {edge_weight_list[i][2]}')
                
                self.__print_line()
                
                self.__basic_operations_screen(graph)

            elif choise == 6:
                vertex = input('\tDigite o vertice -> ')      
                vertices = graph.incidence(vertex)
                
                self.__print_menu_option('basic_operations')
                if len(vertices) == 0:
                    print(f'\t--> Não tem arestas incidentes a {vertex}')
                else:
                    print(f'\t--> Arestas incidentes a {vertex}')
                    self.__print_matrix(vertices)
                
                self.__print_line()
                
                self.__basic_operations_screen(graph)
                
            elif choise == 7:
                vi = input('\tDigite o vertice vi -> ')
                os.system('cls')
                
                is_adjacent = graph.has_vertex(vi)
                if is_adjacent:
                    text = f'{vi} Pertence ao Grafo.'
                else:
                    text = f'{vi} Não Pertence ao Grafo.'
                    
                self.__print_header(text, 'basic_operations')
                self.__basic_operations_screen(graph)
                
            elif choise == 8:
                vi = input('\tDigite o vertice vi -> ')
                vj = input('\tDigite o vertice vj -> ')
                w = input('\tDigite o peso w -> ')

                has_edge = graph.has_edge(vi, vj, w)
                if has_edge:
                    text = f'A Aresta {vi}, {vj} Com Peso {w} Pertencem ao Grafo.'
                else:
                    text = f'A Aresta {vi}, {vj} Com Peso {w} Não Pertencem ao Grafo.'
                
                self.__print_header(text, 'basic_operations')
                self.__basic_operations_screen(graph)

            elif choise == 9:
                self.__print_menu_option('basic_operations')
                self.__print_graph(graph)
                self.__print_line()
                self.__basic_operations_screen(graph)
                
            elif choise == 10:
                self.__print_menu_option('basic_operations')
                print(f'\t--> Matriz de Pesos do Grafo {graph.name}')
                self.__print_matrix(graph.weight_matrix)
                self.__print_line()
                
                self.__basic_operations_screen(graph)
            
            elif choise == 11:
                self.__print_menu_option('basic_operations')
                print(f'\t--> Matriz de Adjacências do Grafo {graph.name}')
                self.__print_adjacency_matrix(graph)
                self.__print_line()
                
                self.__basic_operations_screen(graph)
            
            #Questão 3 - item b - Grafo(G): Retorna uma representação por listas de adjacências de G.
            elif choise == 12:
                self.__print_menu_option('basic_operations')
                print(f'\t--> Lista de Adjacências do Grafo {graph.name}')
                for vertex in graph.adjacency_list:         
                    self.__print_adjacency_lists(graph.adjacency_list, vertex)
                self.__print_line()
                self.__basic_operations_screen(graph)
            
            #Questão 3 - item p - Adjacencia(G, v): Devolve a lista de adjacência de v em G. Deve verificar se v ∈ V (G), caso contrário a operação não poderá ser efetuada.
            elif choise == 13:
                vertex = input('\tDigite o vertice vi -> ')
                self.__print_menu_option('basic_operations')
                print(f'\t--> Lista de Adjacências do Vértice {vertex}')
                
                adjacency_list = graph.get_adjacency_list(vertex)
                self.__print_adjacency_list_vertex(adjacency_list, vertex)
                                
                self.__print_line()
                self.__basic_operations_screen(graph)
                
            elif choise == 14:
                vi = input('\tDigite o vertice vi -> ')
                vj = input('\tDigite o vertice vj -> ')
                
                is_adjacent = graph.check_if_is_adjacent(vi, vj)
                if is_adjacent:
                    text = f'{vi} e {vj} São Adjacentes.'
                else:
                    text = f'{vi} e {vj} Não São Adjacentes.'
                
                self.__print_header(text, 'basic_operations')
                self.__basic_operations_screen(graph)
                
            elif choise == 15:
                is_simple = graph.check_if_the_graph_is_simple()
                if is_simple:
                    text = f'O grafo {graph.name} é simples.'
                else:
                    text = f'O grafo {graph.name} não é simples.'

                self.__print_header(text, 'basic_operations')
                
                self.__basic_operations_screen(graph)
                
            elif choise == 16:
                is_connected = graph.is_connected()
                text = 'O grafo é conexo' if is_connected else 'O grafo é desconexo'

                self.__print_header(text, 'basic_operations')
                self.__basic_operations_screen(graph)
                
            elif choise == 17:
                print('')
                is_bipartite = graph.is_bipartite()
                text = 'O grafo é bipartido' if is_bipartite else 'O grafo não é bipatido'

                self.__print_header(text, 'basic_operations')
                self.__basic_operations_screen(graph)
                
            elif choise == 18:
                print('')
                is_tree = graph.is_tree()
                text = 'O grafo é uma árvore' if is_tree else 'O grafo não é uma árvore'

                self.__print_header(text, 'basic_operations')
                self.__basic_operations_screen(graph)
            
            elif choise == 19:
                complement = graph.complement()
                self.__print_menu_option('basic_operations')
                print(f'\t--> Lista de Adjacências do Grafo {graph.name}')
                print(complement)
                self.__print_line()
                self.__basic_operations_screen(graph)
                
            else:
                raise ExceptionInvalidOperation
        
        except ExceptionGraphHasNoComplement:
            self.__print_header('Não é possível obter o complemento desse grafo!', 'basic_operations')
            self.__basic_operations_screen(graph)
        except ExceptionDoesNotHaveAPathFromViToVj:
            self.__print_header('Não existe um caminho de vi a vj!', 'basic_operations')
            self.__basic_operations_screen(graph)
        except ExceptionCouldNotAddEdge:
            self.__print_header('Não Foi Possível Adicionar Aresta!', 'basic_operations')
            self.__basic_operations_screen(graph)
        except ExceptionVertexDoesNotExist:
            self.__print_header('Vértice Não Existe!', 'basic_operations')
            self.__basic_operations_screen(graph)
        except ExceptionEdgeDoesNotExist:
            self.__print_header('Aresta Não Existe!', 'basic_operations')
            self.__basic_operations_screen(graph)
        except:
            self.__print_header('Opção Inválida. Escolha Novamente!', 'basic_operations')
            self.__basic_operations_screen(graph)


    def __route_screen(self, graph: Graph):
        print('\tTela Anterior (0)')
        print('\tBusca em Largura (1)')
        print('\tBusca em Profundidade (2)\n')

        try:
            choise = int(input('\tEscolha a Opção -> '))
        
            if choise == 0:
                self.__print_header('options')
                self.__options_screen(graph)
            elif choise == 1:
                vi = input('\tDigite o vertice vi -> ')
                search_tree = graph.breadth_first_search(vi)
                self.__print_header(search_tree, 'routes')
                self.__route_screen(graph)
            elif choise == 2:
                vi = input('\tDigite o vertice vi -> ')
                search_tree = graph.depth_first_search(vi)
                self.__print_header(search_tree, 'routes')
                self.__route_screen(graph)
            else:
                raise ExceptionInvalidOperation
                
        except ExceptionInvalidOperation:
            self.__print_header('Opção Inválida. Escolha Novamente!', 'routes')
            self.__route_screen(graph)


    def __shortest_path_screen(self, graph):
        print('\tTela Anterior (0)')
        print('\tCaminho Mínimo Entre Dois Vértices (1)')
        print('\tCustos Mínimos Entre um Vértice e Todos os Outros (2)')
        print('\tCaminhos Mínimos Entre um Vértice e Todos os Outros (3)\n')
        
        try:
            choise = int(input('\tEscolha a Opção -> '))
        
            if choise == 0:
                self.__print_menu_option('options')
                self.__options_screen(graph)
            elif choise == 1:
                vi = input('\tDigite o vertice vi -> ')
                vj = input('\tDigite o vertice vj -> ')
                shortest_path = graph.get_one_shortest_path(vi, vj)
                self.__print_menu_option('shortest_path')
                self.__print_path(shortest_path)
                self.__print_line()
                self.__shortest_path_screen(graph)
                
            elif choise == 2:
                vertex = input('\tDigite o vertice -> ')
                minimal_costs = graph.get_minimal_costs(vertex)
                self.__print_menu_option('shortest_path')
                self.__print_costs(vertex, minimal_costs)
                self.__print_line()
                self.__shortest_path_screen(graph)
                
            elif choise == 3:
                vertex = input('\tDigite o vertice -> ')
                shortest_paths = graph.get_shortest_paths(vertex)
                self.__print_menu_option('shortest_path')
                self.__print_some_paths(shortest_paths)
                self.__print_line()
                self.__shortest_path_screen(graph)
                
            else:
                raise ExceptionInvalidOperation
            
        except ExceptionContainsNegativeCycle:
            self.__print_header('O grafo possui ciclo negativo!', 'shortest_path')
            self.__shortest_path_screen(graph)
        except ExceptionDoesNotHaveAPathFromViToVj:
            self.__print_header('Não existe um caminho de vi a vj!', 'shortest_path')
            self.__shortest_path_screen(graph)
        except ExceptionVertexDoesNotExist:
            self.__print_header('Vértice Não Existe!', 'shortest_path')
            self.__shortest_path_screen(graph)
        except ExceptionEdgeDoesNotExist:
            self.__print_header('Aresta Não Existe!', 'shortest_path')
            self.__shortest_path_screen(graph)
        except ExceptionInvalidOperation:
            self.__print_header('Opção Inválida. Escolha Novamente!', 'shortest_path')
            self.__shortest_path_screen(graph)
        except:
            self.__print_header('Opção Inválida. Escolha Novamente!', 'shortest_path')
            self.__shortest_path_screen(graph)


    def init(self):
        self.__print_menu_option()
        while self.isMenuOpen:
            self.__home_screen()
