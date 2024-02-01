import fibheap as fh


board = [
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1]
]


def h(cur_pos, target_pos):
    return abs(cur_pos[0] - target_pos[0]) + abs(cur_pos[1] - target_pos[1])

def prepare_dis(dis, board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1:
                dis[(i, j)] = fh.Node([float('inf'), (i, j)])

def prepare_path(path, board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1:
                path[(i, j)] = None


def get_neighbours(cur_pos, board):
    directions = []
    if cur_pos[0] - 1 >= 0 and board[cur_pos[0] - 1][cur_pos[1]] == 1:
        directions.append((cur_pos[0] - 1, cur_pos[1]))
    if cur_pos[0] + 1 < len(board) and board[cur_pos[0] + 1][cur_pos[1]] == 1:
        directions.append((cur_pos[0] + 1, cur_pos[1]))
    if cur_pos[1] - 1 >= 0 and board[cur_pos[0]][cur_pos[1] - 1] == 1:
        directions.append((cur_pos[0], cur_pos[1] - 1))
    if cur_pos[1] + 1 < len(board[0]) and board[cur_pos[0]][cur_pos[1] + 1] == 1:
        directions.append((cur_pos[0], cur_pos[1] + 1))
    return directions

def recover_path(path, target):
    res = []
    cur = target
    while path[cur] != None:
        res.append(cur)
        cur = path[cur]
    res.append(cur)
    return res[::-1]

def a_star(soruce, target, board):
    heap = fh.makefheap()

    dis = dict()
    path = dict()
    prepare_dis(dis, board)
    prepare_path(path, board)
    
    dis[soruce].key[0] = h(soruce, target)

    for fh_node in dis.values():
        heap.insert(fh_node)

    while heap.num_nodes != 0:
        cur_path_weight, cur_node= fh.fheappop(heap)
        if cur_node == target and cur_path_weight != float('inf'):
            return recover_path(path, target)
        
        neighbours = get_neighbours(cur_node, board)
        for neighbour in neighbours:
            new_path_weight = cur_path_weight + 1 + h(neighbour, target) - h(cur_node, target)
            if new_path_weight < dis[neighbour].key[0]:
                heap.decrease_key(dis[neighbour], [new_path_weight, neighbour])
                path[neighbour] = cur_node
    return None


print(a_star((0, 0), (5, 6), board))