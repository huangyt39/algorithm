class Solution:
    """
    @param n: An integer
    @return: A list of strings.
    """
    def fizzBuzz(self, n):
        # write your code here
        res = []
        for i in range(1, n + 1):
            if i%3 == 0:
                if i %5 == 0:
                    res.append("fizz buzz")
                else:
                    res.append("fizz")
            else:
                if i %5 == 0:
                    res.append("buzz")
                else:
                    res.append(str(i))
        return res