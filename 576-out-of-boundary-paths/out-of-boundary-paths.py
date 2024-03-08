class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        memo = {}
        
        def recurse(row, col, moves):
            if row >= m or row < 0 or col >= n or col < 0:
                return 1
            if moves == 0:
                return 0

                
            key = (row, col, moves)
            if key in memo:
                return memo[key]
            
            movements = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            res = 0

            for row_disp, col_disp in movements:
                row_ter = row + row_disp
                col_ter = col + col_disp

                res += recurse(row_ter, col_ter, moves - 1)

            memo[key] = res
            return res
        return recurse(startRow, startColumn, maxMove) % (10**9 + 7)