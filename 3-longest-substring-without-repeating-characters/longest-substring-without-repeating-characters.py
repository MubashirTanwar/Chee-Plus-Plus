class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashmap = {}
        l,r,max_len = 0,0,0
        n = len(s)
        while r < n:
            if s[r] in hashmap:
                l = max(l, hashmap[s[r]] + 1)
            hashmap[s[r]] = r
            r+=1
            max_len = max(r-l,max_len)
        return max_len

        