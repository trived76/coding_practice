'''
Runtime: 52 ms, faster than 97.97% of Python3 online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 14.1 MB, less than 54.09% of Python3 online submissions for Longest Substring Without Repeating Characters.
'''

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