class Solution:
    """
    @param board: A list of lists of character
    @param word: A string
    @return: A boolean
    """
    def exist(self, board, word):
        # write your code here
        if len(board) == 0 or len(board[0]) == 0:
            return False
        if len(word) == 0:
            return True
        
        cols, rows = len(board), len(board[0])
        used = [[0]*rows for i in range(cols)]
        # print(used)
        for i in range(cols):
            for j in range(rows):
                if Solution.findWord(1, board, word, cols, rows, i, j, used):
                    return True
        
        return False
    
    def findWord(self, board, word, cols, rows, indexi, indexj, used):
        if len(word) == 0:
            return True
        if indexi < 0 or indexi >= cols:
            return False
        if indexj < 0 or indexj >= rows:
            return False
        # print(board[indexi][indexj])
        # print("word:", word, word[1:])
        # print(used[indexi][indexj] == 0, indexi, indexj)
        # print(board[indexi][indexj] == word[0])
        # print(used)
        if used[indexi][indexj] == 1 or board[indexi][indexj] != word[0]:
            return False
        
        used[indexi][indexj] = 1

        res = Solution.findWord(1, board, word[1:], cols, rows, indexi-1, indexj, used) or Solution.findWord(1, board, word[1:], cols, rows, indexi+1, indexj, used) or Solution.findWord(1, board, word[1:], cols, rows, indexi, indexj+1, used) or Solution.findWord(1, board, word[1:], cols, rows, indexi, indexj-1, used)

        if res == False:
            used[indexi][indexj] = 0
        return res

arr = [

  "ABCE",

  "SFCS",

  "ADEE"

]
word = "ABCCE"
print(Solution.exist(1, arr, word))