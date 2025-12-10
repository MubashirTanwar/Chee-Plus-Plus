class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        hashmap = {
        }

        for index in range(len(nums)):
            if nums[index] in hashmap:
                return [index,hashmap[nums[index]]]
            else:
                hashmap[target - nums[index]] =  index