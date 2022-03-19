'''
Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''

'''
"dvdf", "abb" and "au" were the test cases for which I had to submit my code multiple times

Success
Details 
Runtime: 2673 ms, faster than 5.00% of Python3 online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 14.1 MB, less than 61.13% of Python3 online submissions for Longest Substring Without Repeating Characters.
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ind_start = 0
        max_non_repeat = 0
        curr_ind = 0
        while True:
            list_unique_str = list()
            for i in range(ind_start, len(s)):
                curr_ind = i
                if s[i] not in list_unique_str:
                    list_unique_str.append(s[i])
                else:
                    ind_start += 1
                    break
            max_non_repeat = len(list_unique_str) if max_non_repeat < len(list_unique_str) else max_non_repeat
            if curr_ind >= len(s) - 1:
                break
        return max_non_repeat