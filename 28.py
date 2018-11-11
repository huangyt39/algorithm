class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if matrix == []:
            return False
        matcol = len(matrix)
        matlen = len(matrix[0])
        flag = matcol - 1
        for i in range(matcol):
            if target < matrix[i][0]:
                if i == 0:
                    return False
                else:
                    flag = i - 1
                    break
        for j in range(matlen):
            if target == matrix[flag][j]:
                return True
        return False

