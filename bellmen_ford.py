class my_graph:
    def __init__(self, nodes : list, edges : list):
        self.nodes = nodes
        self.edges = edges
    def add_node(self, node):
        self.nodes.append(node)
    def add_edge(self, edge):      
        self.edges.append(edge)


graph = my_graph(['a', 'b', 'c', 'd', 'e', 'f'], [('a', 'b', 1), ('a', 'c', -2), ('b', 'c', 3), ('c', 'a', 4), ('c', 'b', 5), ('c', 'd', 6), ('d', 'e', 7), ('e', 'f', 8), ('f', 'a', 9), ('f', 'b', -1), ('f', 'c', 11), ('f', 'd', 12), ('f', 'e', -8)])


def init_distance(V, source):
    d = dict()
    for vertex in V:
        d[vertex] = float('inf')
    d[source] = 0
    return d

def init_predecessor(V, source):
    p = dict()
    for vertex in V:
        p[vertex] = None
    return p

def relax(edge, d, p):
    u, v, edge_weight = edge
    if d[v] > d[u] + edge_weight:
        d[v] = d[u] + edge_weight
        p[v] = u

def bellmend_ford(graph, source):
    d = init_distance(graph.nodes, source)
    p = init_predecessor(graph.nodes, source)

    for i in range(len(graph.nodes) - 1):
        for edge in graph.edges:
            relax(edge, d, p)
    

    for edge in graph.edges:
        u, v, edge_weight = edge
        if d[v] > d[u] + edge_weight:
            return None
    return d, p

print(bellmend_ford(graph, 'a'))
        
    



    
