class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        i = 0
        intervals.sort()
        while i < len(intervals)-1:
            if intervals[i][1] >= intervals [i+1][0]:
                if intervals[i][1] > intervals [i+1][1]:
                    intervals.pop(i+1)
                else:
                    intervals[i][1] = intervals[i+1][1]
                    intervals.pop(i+1)
            else:
                i+=1
        
        return intervals