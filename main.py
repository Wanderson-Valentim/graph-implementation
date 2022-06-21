from graph import Graph
from functions import *

data = read_file("graph")
name = data['information'][0]
n = int(data['information'][1])
m = int(data['information'][2])
edges = data['edges']

g1 = Graph(name, n, m, edges)

print(g1.adjacency_list)
print(g1.adjacency_matrix)