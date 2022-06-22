import os
from exceptions import *
from graph import Graph
from functions import *

def home_screen():
    dont_close_program = True
    print('\tGrafo a Partir de Um Arquivo (1)')
    print('\tNovo Grafo (2)')
    print('\tGrafo Salvo (3)')
    print('\tRemove Grafo (4)')
    print('\tFechar (5)\n')
    
    try:
        choise = int(input('\tEscolha a Opção -> '))
        
        if choise == 1:
            data = read_file("graph")
            name = data['information'][0]
            n = int(data['information'][1])
            m = int(data['information'][2])
            edges = data['edges']
            
            save_graph(name, n, m, edges)
            
            graph = Graph(name, n, m, edges)
            os.system('cls')
            print('\n-------------------------------OPÇÕES-------------------------------\n')
            options_screen(graph)
            
        elif choise == 2:
            name = input('\tEscolha o nome do Grafo: ')
            graph = Graph(name)
            save_graph(name)
            os.system('cls')
            print('\n-------------------------------OPÇÕES-------------------------------\n')
            options_screen(graph)
        
        elif choise == 3:
            saved = get_saved_graph()
            was_saved = saved['has_saved_graph']
            
            if was_saved:
                name = saved['graph']['name']
                n = int(saved['graph']['n'])
                m = int(saved['graph']['m'])
                edges = saved['graph']['edges']
                graph = Graph(name, n, m, edges)
                os.system('cls')
                print('\n-------------------------------OPÇÕES-------------------------------\n')
                options_screen(graph)
            else:
                os.system('cls')
                print('\n------------------------IMPLEMENTAÇÃO GRAFOS------------------------\n')
                print('\t--> Não Possui Grafo Salvo!')
                print('\n--------------------------------------------------------------------\n')
            
        elif choise == 4:
            os.system('cls')
            remove_saved_graph()
            print('\n------------------------IMPLEMENTAÇÃO GRAFOS------------------------\n')
            print('\t--> Grafo Removido!')
            print('\n--------------------------------------------------------------------\n')
            
        elif choise == 5:
            dont_close_program = False
            
        else:
            raise ExceptionInvalidOperation
            
    except ExceptionInvalidOperation:
        os.system('cls')
        print('\n------------------------IMPLEMENTAÇÃO GRAFOS------------------------\n')
        print('\t--> Opção Inválida. Escolha Novamente!')
        print('\n--------------------------------------------------------------------\n')
    except:
        os.system('cls')
        print('\n------------------------IMPLEMENTAÇÃO GRAFOS------------------------\n')
        print('\t--> Opção Inválida. Escolha Novamente!')
        print('\n--------------------------------------------------------------------\n')
    
    return dont_close_program
    

def options_screen(graph):
    print('\tTela Anterior (0)')
    print('\tOperações Básicas (1)')
    print('\tPercursos (2)')
    print('\tCaminhos Mínimos (3)\n')
    
    try:
        choise = int(input('\tEscolha a Opção -> '))
        
        if choise == 0:
            os.system('cls')
            print('\n------------------------IMPLEMENTAÇÃO GRAFOS------------------------\n')
            return
            
        elif choise == 1:
            os.system('cls')
            print('\n-------------------------OPERAÇÕES  BÁSICAS-------------------------\n')
            basic_operations_screen(graph)
            
        elif choise == 2:
            os.system('cls')
            print('\n------------------------------PERCURSOS-----------------------------\n')
            route_screen(graph)
            
        elif choise == 3:
            os.system('cls')
            print('\n-------------------------CAMINNHOS  MÍNIMOS-------------------------\n')
            shortest_path_screen(graph)
    
        else:
            raise ExceptionInvalidOperation
            
    except ExceptionInvalidOperation:
        os.system('cls')
        print('\n-------------------------------OPÇÕES-------------------------------\n')
        print('\t--> Opção Inválida. Escolha Novamente!')
        print('\n--------------------------------------------------------------------\n')
        options_screen(graph)
    except NameError:
        print(NameError)
    
    
def basic_operations_screen(graph):
    print('\tTela Anterior (0)')
    print('\tAdicionar Aresta (1)') #OK
    print('\tRemover Aresta (2)') #OK
    print('\tMudar Peso (3)') #Ajustar Excecoes
    print('\tRecupera Peso (4)')
    print('\tIncidência (5)')
    print('\tVerificar se Vértice Pertence ao Grafo (6)') #OK
    print('\tVerificar se Aresta Pertence ao Grafo (7)') #OK
    print('\tImprime Matriz de Adjacências (8)')
    print('\tImprime Lista de Adjacências (9)') #Ok
    print('\tImprime Lista de Adjacências de um Vértice (10)') #OK
    print('\tVerifica se é Vizinho (11)') #OK
    print('\tVerifica se Gafro é Simples (12)')
    print('\tVerifica se Gafro é Conexo (13)')
    print('\tVerifica se Gafro é Bipartido (14)\n')
    
    try:
        choise = int(input('\tEscolha a Opção -> '))
    
        if choise == 0:
            os.system('cls')
            print('\n-------------------------------OPÇÕES-------------------------------\n')
            options_screen(graph)
            
        elif choise == 1:
            vi = input('\tDigite o vertice vi -> ')
            vj = input('\tDigite o vertice vj -> ')
            w = input('\tDigite o peso w -> ')
            os.system('cls')
            print('\n-------------------------OPERAÇÕES  BÁSICAS-------------------------\n')
            
            added_edge = graph.add_edge(vi, vj, w)
            if added_edge:
                save_graph(graph.name, graph.n, graph.m, graph.edges)
                basic_operations_screen(graph)
            else:
                raise ExceptionCouldNotAddEdge
            
        elif choise == 2:
            vi = input('\tDigite o vertice vi -> ')
            vj = input('\tDigite o vertice vj -> ')
            w = input('\tDigite o peso w -> ')
            os.system('cls')
            print('\n-------------------------OPERAÇÕES  BÁSICAS-------------------------\n')
            
            remove_edge = graph.remove_edge(vi, vj, w)
            if remove_edge:
                save_graph(graph.name, graph.n, graph.m, graph.edges)
                basic_operations_screen(graph)
            else:
                raise ExceptionUnableToRemoveEdge
        
        elif choise == 3:
            vi = input('\tDigite o vertice vi -> ')
            vj = input('\tDigite o vertice vj -> ')
            old_w = input('\tDigite o atual peso w -> ')
            new_w = input('\tDigite o novo peso w -> ')
            os.system('cls')
            print('\n-------------------------OPERAÇÕES  BÁSICAS-------------------------\n')
            has_been_changed = graph.change_edge_weight(vi, vj, old_w, new_w)
            
            if has_been_changed:
                save_graph(graph.name, graph.n, graph.m, graph.edges)
                basic_operations_screen(graph)
            else:
                raise ExceptionEdgeDoesNotExist
            
        elif choise == 4:
            '''vi = input('\tDigite o vertice vi -> ')
            vj = input('\tDigite o vertice vj -> ')
            os.system('cls')
            print('\n-------------------------OPERAÇÕES  BÁSICAS-------------------------\n')
            weight = graph.regain_edge_weight(vi, vj)
            print(f'\t--> O Peso da Aresta {vi}, {vj} é {weight}')
            print('\n--------------------------------------------------------------------\n')
            basic_operations_screen(graph)'''
            print('')

        elif choise == 5:
            print('')
            
        elif choise == 6:
            vi = input('\tDigite o vertice vi -> ')
            os.system('cls')
            print('\n-------------------------OPERAÇÕES  BÁSICAS-------------------------\n')
            
            is_adjacent = graph.has_vertex(vi)
            if is_adjacent:
                print(f'\t--> {vi} Pertence ao Grafo.')
            else:
                print(f'\t--> {vi} Não Pertence ao Grafo.')
                
            print('\n--------------------------------------------------------------------\n')
            basic_operations_screen(graph)
            
        elif choise == 7:
            vi = input('\tDigite o vertice vi -> ')
            vj = input('\tDigite o vertice vj -> ')
            w = input('\tDigite o peso w -> ')
            os.system('cls')
            print('\n-------------------------OPERAÇÕES  BÁSICAS-------------------------\n')
            
            has_edge = graph.has_edge(vi, vj, w)
            if has_edge:
                print(f'\t--> A Aresta {vi}, {vj} Com Peso {w} Pertencem ao Grafo.')
            else:
                print(f'\t--> A Aresta {vi}, {vj} Com Peso {w} Não Pertencem ao Grafo.')
                
            print('\n--------------------------------------------------------------------\n')
            basic_operations_screen(graph)
            
        elif choise == 8:
            print('')
            
        elif choise == 9:
            os.system('cls')
            print('\n-------------------------OPERAÇÕES  BÁSICAS-------------------------\n')
            print(f'\t--> Lista de Adjacências do Grafo {graph.name}')
            for vertex in graph.adjacency_list:         
                print_adjacency_list(graph.adjacency_list, vertex)
            print('\n--------------------------------------------------------------------\n')
            basic_operations_screen(graph)
            
        elif choise == 10:
            vertex = input('\tDigite o vertice vi -> ')
            os.system('cls')
            print('\n-------------------------OPERAÇÕES  BÁSICAS-------------------------\n')
            print(f'\t--> Lista de Adjacências do Vértice {vertex}')
            has_vertex = graph.has_vertex(vertex)
            if has_vertex:
                print_adjacency_list(graph.adjacency_list, vertex)
            else:
                raise ExceptionVertexDoesNotExist
            print('\n--------------------------------------------------------------------\n')
            basic_operations_screen(graph)
            
        elif choise == 11:
            vi = input('\tDigite o vertice vi -> ')
            vj = input('\tDigite o vertice vj -> ')
            os.system('cls')
            print('\n-------------------------OPERAÇÕES  BÁSICAS-------------------------\n')
            
            is_adjacent = graph.check_if_is_adjacent(vi, vj)
            if is_adjacent:
                print(f'\t--> {vi} e {vj} São Adjacentes.')
            else:
                print(f'\t--> {vi} e {vj} Não São Adjacentes.')
                
            print('\n--------------------------------------------------------------------\n')
            basic_operations_screen(graph)
            
        elif choise == 12:
            print('')
            
        elif choise == 13:
            print('')
            
        elif choise == 14:
            print('')
            
        else:
            raise ExceptionInvalidOperation
        
    except ExceptionCouldNotAddEdge:
        os.system('cls')
        print('\n-------------------------OPERAÇÕES  BÁSICAS-------------------------\n')
        print('\t--> Não Foi Possível Adicionar Aresta!')
        print('\n--------------------------------------------------------------------\n')
        basic_operations_screen(graph)
    except ExceptionVertexDoesNotExist:
        os.system('cls')
        print('\n-------------------------OPERAÇÕES  BÁSICAS-------------------------\n')
        print('\t--> Vértice Não Existe!')
        print('\n--------------------------------------------------------------------\n')
        basic_operations_screen(graph)
    except ExceptionEdgeDoesNotExist:
        os.system('cls')
        print('\n-------------------------OPERAÇÕES  BÁSICAS-------------------------\n')
        print('\t--> Aresta Não Existe!')
        print('\n--------------------------------------------------------------------\n')
        basic_operations_screen(graph)
    except ExceptionInvalidOperation:
        os.system('cls')
        print('\n-------------------------OPERAÇÕES  BÁSICAS-------------------------\n')
        print('\t--> Opção Inválida. Escolha Novamente!')
        print('\n--------------------------------------------------------------------\n')
        basic_operations_screen(graph)
    except:
        os.system('cls')
        print('\n-------------------------OPERAÇÕES  BÁSICAS-------------------------\n')
        print('\t--> Opção Inválida. Escolha Novamente!')
        print('\n--------------------------------------------------------------------\n')
        basic_operations_screen(graph)


def route_screen(graph):
    print('\tTela Anterior (0)')
    print('\tExcutar Busca em Largura (1)')
    print('\tExcutar Busca em Profundidade (2)\n')

    try:
        choise = int(input('\tEscolha a Opção -> '))
    
        if choise == 0:
            os.system('cls')
            print('\n-------------------------------OPÇÕES-------------------------------\n')
            options_screen(graph)
        elif choise == 1:
            print('')
        elif choise == 2:
            print('')
        else:
            raise ExceptionInvalidOperation
            
    except ExceptionInvalidOperation:
        os.system('cls')
        print('\n------------------------------PERCURSOS-----------------------------\n')
        print('\t--> Opção Inválida. Escolha Novamente!')
        print('\n--------------------------------------------------------------------\n')
        route_screen(graph)


def shortest_path_screen(graph):
    print('\tTela Anterior (0)')
    print('\tCaminhos Mínimos (1)')
    print('\tCustos Mínimos (2)')
    print('\tCaminhos Mínimos Entre um Vértice e Todos os Outros (3)\n')
    
    try:
        choise = int(input('\tEscolha a Opção -> '))
    
        if choise == 0:
            os.system('cls')
            print('\n-------------------------------OPÇÕES-------------------------------\n')
            options_screen(graph)
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
        print('\n-------------------------CAMINNHOS  MÍNIMOS-------------------------\n')
        print('\t--> Opção Inválida. Escolha Novamente!')
        print('\n--------------------------------------------------------------------\n')
        shortest_path_screen(graph)


def menu():
    works = True
    print('\n------------------------IMPLEMENTAÇÃO GRAFOS------------------------\n')
    while works:
        works = home_screen()



menu()