class Solution:
    """
    @param strs: A list of strings
    @return: The longest common prefix
    """
    def longestCommonPrefix(self, strs):
        # write your code here
        if len(strs) == 0:
          return ""
        elif len(strs) == 1:
          return strs[0]
        res = strs[0]
        for string in strs:
          if string == "":
            return ""
          for char_index in range(len(string)):
            if char_index >= len(res):
              break
            if res[char_index] != string[char_index]:
              res = string[0:char_index]
              break
        return res

A = ["ABCD", "ABCEF", "ABCEDF"]
print(Solution.longestCommonPrefix(A, A))