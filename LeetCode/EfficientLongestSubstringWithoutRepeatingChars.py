class Solution:   
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        max_len = 0
        d = dict()
        
        for i in range(len(s)):
            if s[i] not in d:
                max_len = max(max_len, i - start + 1)
            else:
                if d[s[i]] >= start:
                    start = d[s[i]] + 1
                else:
                    max_len = max(max_len, i - start + 1)    
            d[s[i]] = i
        return max_len