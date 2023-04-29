class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row,col = set(),set()
        n, m = len(matrix[0]), len(matrix)
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)
        
        for i in row:
            for j in range(n):
                matrix[i][j] = 0
        for j in col:
            for i in range(m):
                matrix[i][j] = 0
