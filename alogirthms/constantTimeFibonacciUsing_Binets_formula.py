class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        #more information about this formula can be found here -> http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/fibFormula.html
        #for high value of n this may give wrong result, but for this problem it was accepted
        n +=1
        num = 1.618033988749895**n - (-0.6180339887498949)**n
        denom = 2.23606797749979
        return int(num/denom)
