import array

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        for i in range(len(nums)):
            hashmap = {}
            for j in range(i+1, len(nums)):
                k = - (nums[i] + nums[j])
                if k in hashmap:
                    arr = [nums[i], nums[j], k]
                    arr.sort()
                    ans.append(arr)
                    hashmap.pop(k)
                else:
                    hashmap[nums[j]] = nums[j]
        unique_tuples = set(tuple(x) for x in ans)
        unique_lists = [list(x) for x in unique_tuples]
        return unique_lists