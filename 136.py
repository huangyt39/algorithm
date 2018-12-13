class Solution:
    """
    @param: s: A string
    @return: A list of lists of string
    """
    def partition(self, s):
        # write your code here
        if not s:
            return
        
        if len(s) == 1:
            return [[s]]
        res = []
        substrMaps = self.substr(s)
        for substrMap in substrMaps:
            if not substrMap[1]:
                res.append([substrMap[0]])
                continue
            nextsubstr = self.partition(substrMap[1])
            for i in nextsubstr:
                tmp = i[:]
                tmp.insert(0, substrMap[0])
                res.append(tmp)
        return res
        
    def substr(self, s):
        if not s:
            return
        
        if len(s) == 1:
            return [[s,""]]
        res = []
        for i in range(0, len(s)):
            head, tail = 0, i
            while head < tail:
                if s[head] != s[tail]:
                    break
                head += 1
                tail -= 1
            if head >= tail:
                res.append([s[:i+1], s[i+1:]])
        return res