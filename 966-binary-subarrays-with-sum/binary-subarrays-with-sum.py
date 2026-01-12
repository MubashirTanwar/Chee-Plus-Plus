class Solution(object):
    def subArrayWithSum(self, nums, goal):
        if(goal < 0):
            return 0
        l, r, sum, count = 0,0,0,0
        while(r < len(nums)):
            sum+=nums[r]
            while sum > goal:
                sum-=nums[l]
                l+=1
            count+=r-l+1
            r+=1
        return count
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        return self.subArrayWithSum(nums, goal) - self.subArrayWithSum(nums, goal-1)
        