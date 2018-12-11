class Solution:
    """
    @param str: str: the given string
    @return: char: the first unique character in a given string
    """
    def firstUniqChar(self, str):
        # Write your code here
        if not str:
            return 
        
        dic, arr = {}, []
        for char in str:
            if char not in dic:
                dic[char] = 1
                arr.append(char)
            else:
                dic[char] += 1
                
        for item in arr:
            if dic[item] == 1:
                return item