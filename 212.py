class Solution:
    # @param {char[]} string: An array of Char
    # @param {int} length: The true length of the string
    # @return {int} The true length of new string
    def replaceBlank(self, string, length):
        # Write your code here
        if string is None:
            return 0
        count = length
        for s in string:
            if count != 0:
                count -= 1
                if s != ' ':
                    string.append(s)
                else:
                    string.append('%')
                    string.append('2')
                    string.append('0')
        for i in range(length):
            string.pop(0)
        return len(string)
        
print(Solution.replaceBlank(1, "hello world", 11))