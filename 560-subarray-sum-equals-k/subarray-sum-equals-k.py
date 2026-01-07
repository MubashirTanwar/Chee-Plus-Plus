class Solution(object):
    def subarraySum(self, nums, k):
        count = 0
        prefix_sum = 0
        sums = {0: 1}

        for num in nums:
            prefix_sum += num
            if prefix_sum - k in sums:
                count += sums[prefix_sum - k]
            sums[prefix_sum] = sums.get(prefix_sum, 0) + 1

        return count
