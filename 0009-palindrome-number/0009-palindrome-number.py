class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        y = "".join([i for i in x][::-1])
        return x == y
        