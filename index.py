def read_file(path):
    data = {
        'information': [],
        'edges': []
    }
    is_first_iteration = True
    
    with open(path) as file:
        for line in file:
            if(is_first_iteration):
                is_first_iteration = False
                data['information'] = line.split()
            elif(line == '\n'):
                continue
            else:
                data['edges'].append(line.split())
    
    return data
                
def generate_adjacency_list(edges):
    adjacency_list = {}
    
    for edge in edges:
        vertex_in_the_adj_list = edge[0] in list(adjacency_list.keys())
        
        if(vertex_in_the_adj_list):
            adjacency_list[edge[0]].append(edge[1])
        else:
            adjacency_list[edge[0]] = [edge[1]]
    
    return adjacency_list


g = read_file("graph.txt")

print(generate_adjacency_list(g['edges']))
