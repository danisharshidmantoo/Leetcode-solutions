class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rowZero,colZero = False, False
        rows,cols = len(matrix),len(matrix[0])
        for r in range(rows):
            if matrix[r][0] == 0:
                colZero = True
        for c in range(cols):
            if matrix[0][c] == 0:
                rowZero = True
        for r in range(1,rows):
            for c in range(1,cols):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
        for r in range(1,rows):
            if matrix[r][0] == 0:
                for c in range(cols):
                    matrix[r][c] = 0
        for c in range(1,cols):
            if matrix[0][c] == 0:
                for r in range(rows):
                    matrix[r][c] = 0
        if rowZero:
            for c in range(cols):
                matrix[0][c] = 0
        if colZero:
            for r in range(rows):
                matrix[r][0] = 0

