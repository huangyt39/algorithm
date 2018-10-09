class Solution:
    """
    @param matrix: A list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if len(matrix) == 0:
            return 0
        if len(matrix[0]) == 0:
            return 0
        res = 0
        n, m = len(matrix[0]), len(matrix)
        x, y = 0, 0
        while x != n and y != m:
            if matrix[y][x] == target:
                res += 1
            for i in range(x + 1, n):
                if matrix[y][i] == target:
                    res += 1
                    break
            for j in range(y + 1, m):
                if matrix[j][x] == target:
                    res += 1
                    break
            x += 1
            y += 1
        return res

# print(Solution.searchMatrix(1, [[1,3,5,7],[2,4,7,8],[3,5,9,10]], 3))
print(Solution.searchMatrix(1, [[3,4]], 3))
print(Solution.searchMatrix(1, [[1,3,5,7],[3,11,16,20],[23,30,34,50]], 3))