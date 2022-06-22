import os
from graph import Graph
from functions import *

def home_screen():
    dont_close_program = True
    
    print('Grafo a Partir de Um Arquivo (1)')
    print('Novo Grafo (2)')
    print('Grafo Salvo (3)')
    print('Remove Grafo (4)')
    print('Fechar (5)')
    
    try:
        choise = int(input('Escolha a Opção: '))
        
        if choise == 1:
            data = read_file("graph")
            name = data['information'][0]
            n = int(data['information'][1])
            m = int(data['information'][2])
            edges = data['edges']
            
            save_graph(name, n, m, edges)
            
            graph = Graph(name, n, m, edges)
            options_screen(graph)
            
        elif choise == 2:
            name = input('Escolha o nome do Grafo: ')
            graph = Graph(name)
            save_graph(name)
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
                options_screen(graph)
            else:
                print('Não Possui Grafo Salvo!')
            
        elif choise == 4:
            remove_saved_graph()
            print('Grafo Removido!')
            
        elif choise == 5:
            dont_close_program = False
            
        else:
            os.system('cls')
            print('Opção Inválida. Escolha Novamente!')
            home_screen()
            
    except(NameError):
        print(NameError)
        #os.system('cls')
        print('Opção Inválida. Escolha Novamente!')
        home_screen()
    
    return dont_close_program
    

def options_screen(graph):
    os.system('cls')
    print('Tela Anterior (0)')
    print('Operações Básicas (1)')
    print('Percursos (2)')
    print('Caminhos Mínimos (3)')
    
    try:
        choise = int(input('Escolha a Opção: '))
        
        if choise == 0:
            os.system('cls')
            home_screen()
            
        elif choise == 1:
            basic_operations_screen(graph)
            
        elif choise == 2:
            route_screen(graph)
            
        elif choise == 3:
            shortest_path_screen(graph)
    
        else:
            os.system('cls')
            print('Opção Inválida. Escolha Novamente!')
            options_screen()
            
    except:
        os.system('cls')
        print('Opção Inválida. Escolha Novamente!')
        options_screen()
    
def basic_operations_screen(graph):
    os.system('cls')
    print('Tela Anterior (0)')
    print('Adicionar Aresta ()')
    print('Remover Aresta ()')
    print('Verificar se Vértice Pertence ao Grafo ()')
    print('Verificar se Aresta Pertence ao Grafo ()')
    print('Mudar Peso ()')
    print('Recupera Peso ()')
    print('Incidência ()')
    print('Imprime Lista de Adjacências de um Vértice ()')
    print('Imprime Lista de Adjacências ()')
    print('Imprime Matriz de Adjacências ()')
    print('Verifica se Gafro é Simples ()')
    print('Verifica se Gafro é Conexo ()')
    print('Verifica se Gafro é Bipartido ()')
    print('Verifica se é Vizinho ()')
    
    choise = input('Escolha a Opção: ')
    
    if choise == 1:
        print('')
    '''elif choise == 2:
    elif choise == 3:
    elif choise == 4:
    else:'''
    

def route_screen(graph):
    print('Tela Anterior (0)')
    print('Excutar Busca em Largura (1)')
    print('Excutar Busca em Profundidade (2)')

    
    choise = input('Escolha a Opção: ')
    
    if choise == 1:
        print('')
    '''elif choise == 2:
    elif choise == 3:
    elif choise == 4:
    else:'''

def shortest_path_screen(graph):
    print('Tela Anterior (0)')
    print('Caminhos Mínimos (1)')
    print('Custos Mínimos (2)')
    print('Caminhos Mínimos Entre um Vértice e Todos os Outros (3)')
    
    choise = input('Escolha a Opção: ')
    
    if choise == 1:
        print('')
    '''elif choise == 2:
    elif choise == 3:
    elif choise == 4:
    else:'''

def menu():
    works = True
    
    while works:
        works = home_screen()

menu()
#os.system('cls')