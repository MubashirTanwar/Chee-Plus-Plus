import array

class Solution(object):
    def next_best(self,nums, idx):
        next_idx =idx
        while nums[idx] == nums[next_idx]:
            next_idx+=1
            if(next_idx == len(nums)-1):
                return next_idx
        return next_idx
    
    def prev_best(self,nums, idx):
        prev_idx = idx
        while nums[idx] == nums[prev_idx]:
            prev_idx-=1
            if(prev_idx == 0):
                return prev_idx
        return prev_idx
    
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        i = 0
        j = 1
        k = len(nums) -1
        nums.sort()

        ans = []
        while i < k:
            while j < k:
                arr_sum = nums[i] + nums[j] + nums[k]
                if arr_sum == 0:
                    ans.append([nums[i], nums[j], nums[k]])
                    j = self.next_best(nums,j)
                elif arr_sum > 0:
                    k = self.prev_best(nums, k)
                else:
                    j = self.next_best(nums,j)
            
            i =self.next_best(nums,i)
            j = i+1
            k = len(nums) -1
        return ans


