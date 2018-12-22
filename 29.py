class Solution:
    """
    @param s1: A string
    @param s2: A string
    @param s3: A string
    @return: Determine whether s3 is formed by interleaving of s1 and s2
    """
    def isInterleave(self, s1, s2, s3):
        # write your code here
        if not s3:
            if not s1 and not s2:
                return True
            else:
                return False
        else:
            if not s1 and not s2:
                return False
            if not s1:
                if s2 == s3:
                    return True
                else:
                    return False
            if not s2:
                if s1 == s3:
                    return True
                else:
                    return False
        
        if s3[0] == s1[0] and s3[0] == s2[0]:
            return self.isInterleave(s1[1:], s2, s3[1:]) or self.isInterleave(s1, s2[1:], s3[1:])
        elif s3[0] == s1[0]:
            return self.isInterleave(s1[1:], s2, s3[1:])
        elif s3[0] == s2[0]:
            return self.isInterleave(s1, s2[1:], s3[1:])
            
        return False