def read_file(path):
    with open(path) as file:
        for line in file:
            if(line == '\n'):
                pass
            else:
                yield line.split()
                
def generate_adjacency_list(path):
    adjacency_list = {}
    is_first_iteration = True
    
    for element in (read_file(path)):
        if(is_first_iteration):
            is_first_iteration = False
            graph = {
                'name': element[0],
                'n': element[1],
                'm': element[2],
            }
        else:
            element_in_the_adj_list = element[0] in list(adjacency_list.keys())
            
            if(element_in_the_adj_list):
                adjacency_list[element[0]].append(element[1])
            else:
                adjacency_list[element[0]] = [element[1]]
                
    graph['adjacency_list'] = adjacency_list
    
    return graph


print(generate_adjacency_list("graph.txt"))
