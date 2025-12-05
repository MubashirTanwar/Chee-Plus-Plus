class Solution(object):
    # def calculate(self, i,j):
    #     if(i == 0 or j == 0):
    #         return 1
    #     return self.calculate(i,j-1) + self.calculate(i-1,j)
    
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        n = m+n-2
        m = m-1
        cost = 1
        for index in range(1,m+1):
            cost = cost* (n-m+index)/index
        return cost