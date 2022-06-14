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

def createNode(graph, key, neighboor, weight):
    if key in graph:
        graph[key][neighboor] = weight
    else:
        graph[key] = {}
        graph[key][neighboor] = weight

def generate_adjacency_list(edges):
    graph = {}
    for edge in edges:
        key = edge[0]
        if(len(edge) > 1):
            neighbor = edge[1]
            weight = edge[2]
            createNode(graph, key, neighbor, weight)
    
    return graph

def generate_adjacency_matrix(edges):
    adjacency_matrix = [[0 for _ in range(5)] for _ in range(5)]
    
    for edge in edges:
        vertex1 = edge[0]
        vertex2 = edge[1]
        vi = int(vertex1[1]) - 1
        vj = int(vertex2[1]) - 1
        adjacency_matrix[vi][vj] = 1

    return adjacency_matrix

g = read_file("graph.txt")

t = generate_adjacency_list(g['edges'])

print(t)
