import json
from graph import Graph

#Questão 1
def read_file(file_name):
    data = {
        'information': [],
        'edges': []
    }
    is_first_iteration = True
    
    with open(f'./graphs/{file_name}.txt') as file:
        for line in file:
            if(is_first_iteration):
                is_first_iteration = False
                data['information'] = line.split()
            elif(line == '\n'):
                continue
            else:
                data['edges'].append(line.split())
    
    return data

#Salvamento de Grafos em JSON
def get_saved_graph():
    with open('./settings/saved_graph.json') as my_json:
        saved_graph = json.load(my_json)
    
    return saved_graph

def write_to_file_json(data):
    saved_graph = json.dumps(data, indent=4)
    with open('./settings/saved_graph.json', 'w') as file:
        file.write(saved_graph)
        
def save_graph(name, n = 1, m = 0, edges = []):
    data = {
        'has_saved_graph': True,
        'graph':{}
    }

    data['graph']['name'] = name
    data['graph']['n'] = str(n)
    data['graph']['m'] = str(m)
    data['graph']['edges'] = edges

    write_to_file_json(data)

def remove_saved_graph():
    data = {
        'has_saved_graph': False,
        'graph':{}
    }
    
    data['graph']['name'] = ''
    data['graph']['n'] = ''
    data['graph']['m'] = ''
    data['graph']['edges'] = []
    
    write_to_file_json(data)
    
def print_adjacency_list(adjacency_list, vi):
    print(f'\t[{vi}] --> ', end='')
    for vertex in adjacency_list[vi]:
        print(f'[{vertex}] --> ', end='')
    print('λ')