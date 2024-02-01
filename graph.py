import heapq
import fibheap as fh


class node:
    def __init__(self, name):
        self.name = name
        self.connections = []
        self.visited = False
    
    def add_connection(self, connection):
        self.connections.append(connection)
    
    def print_connections(self):
        print(f'{self.name}: ')
        for connection in self.connections:
            print(f'{connection[0].name} cost {connection[1]}')

    def __lt__(self, other):
        return self.name < other.name


# make a very complicated graph with 10 nodes

a = node('A')
b = node('B')
c = node('C')
d = node('D')
e = node('E')
f = node('F')

a.add_connection((b, 1))
a.add_connection((c, 2))
b.add_connection((c, 3))
c.add_connection((a, 4))




def bfs(node):
    q = []
    discovered = set()
    q.append(node)
    res = []
    discovered.add(node.name)
    while len(q) > 0:
        curr = q.pop(0)
        res.append(curr)
        for connection in curr.connections:
            if connection[0].name not in discovered:
                q.append(connection[0])
                discovered.add(connection[0].name)
    return res


def dijskra_binary_heap(soruce):
    pq = []
    heapq.heapify(pq)
    heapq.heappush(pq, (0, soruce))
    expored = set()
    while len(pq) > 0:
        cur_path_weight, cur_node,= heapq.heappop(pq)
        if cur_node.name in expored:
            continue
        expored.add(cur_node.name)
        print(f'explored {cur_node.name} min cost is {cur_path_weight} from source node {soruce.name}')
        for con_node, edge_weight in cur_node.connections:
            if con_node.name in expored:
                continue

            heapq.heappush(pq,(edge_weight + cur_path_weight, con_node))

# dijskra_binary_heap(a)

def dijskra_fib_heap(soruce):
    heap = fh.makefheap()
    vertices = bfs(soruce)
    dis = dict()
    for v in vertices:
        dis[v.name] = fh.Node([float('inf'), v])
    
    dis[soruce.name].key[0] = 0

    for fh_node in dis.values():
        heap.insert(fh_node)

    while heap.num_nodes != 0:
        cur_path_weight, cur_node = fh.fheappop(heap)
        print(f'explored {cur_node.name} min cost is {cur_path_weight} from source node {soruce.name}')
        for con_node, edge_weight in cur_node.connections:
            new_path_weight = cur_path_weight + edge_weight
            if new_path_weight < dis[con_node.name].key[0]:
                heap.decrease_key(dis[con_node.name], [new_path_weight, con_node])



dijskra_fib_heap(a)

