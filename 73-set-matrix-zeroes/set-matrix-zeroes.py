class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        r, c = set(), set()

        # Identifying rows and columns to be zeroed
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    r.add(i)
                    c.add(j)
        
        # Setting the identified columns to zero
        for j in c:
            for i in range(m):
                matrix[i][j] = 0
        
        # Setting the identified rows to zero
        for i in r:
            for j in range(n):
                matrix[i][j] = 0
