class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def recurse(cur_str, pos, visited):
            i, j = pos
            if (i < 0 or i >= m or j < 0 or j >= n or 
                visited[i][j] or board[i][j] != word[len(cur_str)]):
                return False
            
            cur_str += board[i][j]
            if len(cur_str) == len(word):
                return True

            visited[i][j] = True  # Mark the current position as visited
            for ver_mov, hor_mov in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                next_pos = (i + ver_mov, j + hor_mov)
                if recurse(cur_str, next_pos, visited):
                    return True
            visited[i][j] = False  # Reset the position for backtracking

            return False

        visited = [[False for _ in range(n)] for _ in range(m)]
        return any(recurse('', (i, j), visited) for i in range(m) for j in range(n))
