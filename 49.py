class Solution:
    """
    @param: chars: The letter array you should sort by Case
    @return: nothing
    """
    def sortLetters(self, chars):
        # write your code here
        if len(chars) == 0:
            return chars
        i = 0
        j = len(chars) - 1
        while True:
            while i != j and chars[j].isupper():
                j -= 1
            while i != j and chars[i].islower():
                i += 1
            if i == j :
                break
            temp = chars[i]
            chars[i] = chars[j]
            chars[j] = temp
        return chars

strr = ['A','c']
print(Solution.sortLetters(strr, strr))
