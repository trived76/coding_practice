'''
Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
'''

'''
Issue: Time Limit Exceeded
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
   
        if len(s) <= 1:
            return s

        if len(set(s)) == 1:
            return s

        max_len = 0
        start = 0
        s_out = ""

        while True:
            for i in range(start+1,len(s)+1,1):
                if s[start:i] == s[start:i][::-1]:
                    if max_len < len(s[start:i]):
                        max_len = max(max_len, len(s[start:i]))
                        s_out = s[start:i]
            start += 1
            if start > len(s):
                break
        return s_out