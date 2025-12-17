
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashmap = {}
        if(len(nums)<1):
            return 0
        for num in nums:
            if num in hashmap:
                continue
            if(num+1 in hashmap):
                hashmap[num]= num+1
            if(num-1 in hashmap):
                hashmap[num-1] = num
            if(num not in hashmap):
                hashmap[num] = None
        
        max_count = 1
        length_cache = {}

        for item in hashmap:
            if item in length_cache:
                continue

            current = item
            stack = []

            while current is not None and current not in length_cache:
                stack.append(current)
                current = hashmap[current]

            # if we hit a known length, use it; otherwise start from 0
            count = length_cache[current] if current in length_cache else 0

            # backfill lengths
            while stack:
                count += 1
                length_cache[stack.pop()] = count

            max_count = max(max_count, length_cache[item])

        return max_count
