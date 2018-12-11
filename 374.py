class Solution:
    """
    @param matrix: a matrix of m x n elements
    @return: an integer list
    """
    def spiralOrder(self, matrix):
        # write your code here
        if not matrix:
            return []
            
        res = []
        m,n = len(matrix), len(matrix[0])
        
        startX, startY, endX, endY = 0, 0, n-1, m-1
        
        while startX <= endX and startY <= endY:
            for i in range(startX, endX+1):
                res.append(matrix[startY][i])
            
            if startY < endY:
                for i in range(startY+1, endY+1):
                    res.append(matrix[i][endX])
                
            if startX < endX:
                for i in range(endX-1, startX-1, -1):
                    res.append(matrix[endY][i])
                    
            if startY < endY:
                for i in range(endY-1, startY, -1):
                    res.append(matrix[i][startX])
                    
            startX += 1
            endX -= 1
            startY += 1
            endY -= 1
            
        return res