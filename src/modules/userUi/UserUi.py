import os
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
        print('-' * self.text_size)


    def __print_text(self, text: str):
        size = int((self.text_size - len(text)) / 2)
        space = ' ' * size
        print(f'{space}{text}{space}\n')

    
    def __print_header(self, text: str, option = 'graphs'):
        self.__print_menu_option(option)
        self.__print_text(f'--> {text} <--')
        self.__print_line()


    def __graph_from_file(self):
        data = read_file("graph")
        name = data['information'][0]
        n = int(data['information'][1])
        m = int(data['information'][2])
        edges = data['edges']
        save_graph(name, n, m, edges)
        graph = Graph(name, n, m, edges)
        self.__print_menu_option('options')
        self.__options_screen(graph)
    

    def __new_graph(self):
        name = input('\tEscolha o nome do Grafo: ')
        graph = Graph(name)
        save_graph(name)
        self.__print_text('options')
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
            self.__print_text('options')
            self.__options_screen(graph)
        else:
            self.__print_header('Não Possui Grafo Salvo!')
    

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
                options[home_screen_option - 1][1]()
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
            print(not(option in range(0, 4)))
        except NameError:
            print(NameError)


    def __basic_operations_screen(self, graph):
        print('\tTela Anterior (0)')
        print('\tAdicionar Vértices (1)') #OK
        print('\tAdicionar Aresta (2)') #OK
        print('\tRemover Aresta (3)') #OK
        print('\tMudar Peso (4)') #Ajustar Excecoes
        print('\tRecupera Peso (5)')
        print('\tIncidência (6)')
        print('\tVerificar se Vértice Pertence ao Grafo (7)') #OK
        print('\tVerificar se Aresta Pertence ao Grafo (8)') #OK
        print('\tImprime Matriz de Adjacências (9)')
        print('\tImprime Lista de Adjacências (10)') #Ok
        print('\tImprime Lista de Adjacências de um Vértice (11)') #OK
        print('\tVerifica se é Vizinho (12)') #OK
        print('\tVerifica se Gafro é Simples (13)')
        print('\tVerifica se Gafro é Conexo (14)')
        print('\tVerifica se Gafro é Bipartido (15)\n')

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
                self.__print_menu_option('c')
                has_been_changed = graph.change_edge_weight(vi, vj, old_w, new_w)
                
                if has_been_changed:
                    save_graph(graph.name, graph.n, graph.m, graph.edges)
                    self.__basic_operations_screen(graph)
                else:
                    raise ExceptionEdgeDoesNotExist
                
            elif choise == 5:
                print('')

            elif choise == 6:
                print('')
                
            elif choise == 7:
                vi = input('\tDigite o vertice vi -> ')
                os.system('cls')
                
                is_adjacent = graph.has_vertex(vi)
                if is_adjacent:
                    text = f'\t--> {vi} Pertence ao Grafo.'
                else:
                    text = f'\t--> {vi} Não Pertence ao Grafo.'
                    
                self.__print_header(text, 'basic_operations')
                self.__basic_operations_screen(graph)
                
            elif choise == 8:
                vi = input('\tDigite o vertice vi -> ')
                vj = input('\tDigite o vertice vj -> ')
                w = input('\tDigite o peso w -> ')

                has_edge = graph.has_edge(vi, vj, w)
                if has_edge:
                    text = f'\t--> A Aresta {vi}, {vj} Com Peso {w} Pertencem ao Grafo.'
                else:
                    text = f'\t--> A Aresta {vi}, {vj} Com Peso {w} Não Pertencem ao Grafo.'
                
                self.__print_header(text, 'basic_operations')
                self.__basic_operations_screen(graph)
                
            elif choise == 9:
                print('')
                
            elif choise == 10:
                self.__print_menu_option('basic_operations')
                print(f'\t--> Lista de Adjacências do Grafo {graph.name}')
                for vertex in graph.adjacency_list:         
                    print_adjacency_list(graph.adjacency_list, vertex)
                self.__print_line()
                self.__basic_operations_screen(graph)
                
            elif choise == 11:
                vertex = input('\tDigite o vertice vi -> ')
                self.__print_menu_option('basic_operations')
                print(f'\t--> Lista de Adjacências do Vértice {vertex}')
                has_vertex = graph.has_vertex(vertex)
                if has_vertex:
                    print_adjacency_list(graph.adjacency_list, vertex)
                else:
                    raise ExceptionVertexDoesNotExist
                                
                self.__print_line()
                self.__basic_operations_screen(graph)
                
            elif choise == 12:
                vi = input('\tDigite o vertice vi -> ')
                vj = input('\tDigite o vertice vj -> ')
                os.system('cls')
                
                is_adjacent = graph.check_if_is_adjacent(vi, vj)
                if is_adjacent:
                    text = f'\t--> {vi} e {vj} São Adjacentes.'
                else:
                    text = f'\t--> {vi} e {vj} Não São Adjacentes.'
                
                self.__print_header(text, 'basic_operations')
                self.__basic_operations_screen(graph)
                
            elif choise == 13:
                print('')
                
            elif choise == 14:
                print('')
                
            elif choise == 15:
                print('')
                
            else:
                raise ExceptionInvalidOperation
            
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


    def __route_screen(self, graph):
        print('\tTela Anterior (0)')
        print('\tBusca em Largura (1)')
        print('\tBusca em Profundidade (2)\n')

        try:
            choise = int(input('\tEscolha a Opção -> '))
        
            if choise == 0:
                self.__print_header('options')
                self.__options_screen(graph)
            elif choise == 1:
                print('')
            elif choise == 2:
                vi = input('\tDigite o vertice vi -> ')
                search_tree = graph.depth_first_search(vi)
                self.__print_header(search_tree, 'routes')
                self.__route_screen(graph)
            else:
                raise ExceptionInvalidOperation
                
        except ExceptionInvalidOperation:
            os.system('cls')
            self.__print_header('Opção Inválida. Escolha Novamente!', 'routes')
            self.__route_screen(graph)


    def __shortest_path_screen(self, graph):
        print('\tTela Anterior (0)')
        print('\tCaminhos Mínimos (1)')
        print('\tCustos Mínimos (2)')
        print('\tCaminhos Mínimos Entre um Vértice e Todos os Outros (3)\n')
        
        try:
            choise = int(input('\tEscolha a Opção -> '))
        
            if choise == 0:
                self.__print_header('options')
                self.__options_screen(graph)
            elif choise == 1:
                print('')
            elif choise == 2:
                print('')
            elif choise == 3:
                print('')
            else:
                raise ExceptionInvalidOperation
                
        except ExceptionInvalidOperation:
            os.system('cls')
            self.__print_header('Opção Inválida. Escolha Novamente!', 'shortest_path')
            self.__shortest_path_screen(graph)


    def init(self):
        self.__print_menu_option()
        while self.isMenuOpen:
            self.__home_screen()
