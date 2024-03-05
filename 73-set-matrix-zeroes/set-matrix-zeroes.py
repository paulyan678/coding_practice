class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][j] = 1.1
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1.1:
                    matrix[i][j] == 0

                    for k in range(m):
                        if matrix[k][j] == 1.1:
                            continue
                        matrix[k][j] = 0

                    for k in range(n):
                        if matrix[i][k] == 1.1:
                            continue
                        matrix[i][k] = 0
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1.1:
                    matrix[i][j] = 0
        