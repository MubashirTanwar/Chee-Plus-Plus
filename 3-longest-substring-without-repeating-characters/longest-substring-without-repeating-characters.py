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
            # while s[r] not in hashmap:
            if s[r] in hashmap:
                print(s[r], "in hashmap", hashmap[s[r]] )
                # l=hashmap[s[r]] +1
                l = max(l, hashmap[s[r]] + 1)

            
            hashmap[s[r]] = r
            r+=1
            
            max_len = max(r-l,max_len)
            print(max_len,l,r)
        print(hashmap)
        return max_len

        