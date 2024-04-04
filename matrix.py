
def updateMatrix(mat):
    m, n = len(mat), len(mat[0])
    res_mat = [[-1]*n for _ in range(m)]
    
    def recurse(i, j):
        if res_mat[i][j] != -1:
            return res_mat[i][j]
        
        if mat[i][j] == 0:
            res_mat[i][j] = 0
            return 0

        disp = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        cur_res = n*m
        for row_disp, col_disp in disp:
            i_ter = i + row_disp
            j_ter = j + col_disp
            if i_ter < 0 or i_ter >= m or j_ter < 0 or j_ter >= n:
                continue
            
            cur_res = min(cur_res, recurse(i_ter, j_ter) + 1)
        res_mat[i][j] = cur_res
        return cur_res
    for i in range(m):
        for j in range(n):
            recurse(i, j)
    return res_mat

print(updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))

def bfs_updateMatrix(mat):
    m, n = len(mat), len(mat[0])
    res_mat = [[-1]*n for _ in range(m)]
    queue = []
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:
                res_mat[i][j] = 0
                queue.append((i, j))
    while queue:
        i, j = queue.pop(0)
        disp = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for row_disp, col_disp in disp:
            i_ter = i + row_disp
            j_ter = j + col_disp
            if i_ter < 0 or i_ter >= m or j_ter < 0 or j_ter >= n or res_mat[i_ter][j_ter] != -1:
                continue
            res_mat[i_ter][j_ter] = res_mat[i][j] + 1
            queue.append((i_ter, j_ter))
    return res_mat