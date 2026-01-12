class Solution(object):
    def allSubarrays(self,nums,k):
        l,r,sum,count = 0,0,0,0
        while (r < len(nums)):
            sum+=nums[r]%2
            while sum > k:
                sum-=nums[l]%2
                l+=1
            count+=r-l+1
            r+=1
        return count
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.allSubarrays(nums,k) - self.allSubarrays(nums,k-1)