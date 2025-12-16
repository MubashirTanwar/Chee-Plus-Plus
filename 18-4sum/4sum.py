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
    
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        i = 0
        j = 1
        k = 2
        n = len(nums)
        l = n -1
        if (l < 3):
            return []
        nums.sort()

        ans = []
        while i < n-3:
            while j < n-2:
                while k < l:
                    addit = nums[i] + nums[j] + nums[k] + nums[l]
                    if addit == target:
                        ans.append([nums[i], nums[j], nums[k], nums[l]])
                        k = self.next_best(nums,k)
                        l = self.prev_best(nums,l)
                    elif addit < target:
                        k = self.next_best(nums,k)
                    else:
                        l = self.prev_best(nums,l)
                
                j = self.next_best(nums,j)
                k = j+1
                l = n-1
            i = self.next_best(nums,i)
            j=i+1
            k = j+1
            l = n-1
        return ans