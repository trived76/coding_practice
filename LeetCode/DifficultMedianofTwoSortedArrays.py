'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
'''


'''
Runtime: 96 ms, faster than 90.42% of Python3 online submissions for Median of Two Sorted Arrays.
Memory Usage: 14.1 MB, less than 71.96% of Python3 online submissions for Median of Two Sorted Arrays.
'''
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        n = n1 + n2
        if n % 2 == 0:
            median_idx = [(n // 2) - 1, n // 2]
        else:
            median_idx = [n // 2]
            
        m = 0
        a1 = 0
        a2 = 0

        for i in range(n):
            nm1_bool = False
            nm2_bool = False
            
            final_put = -1000001
            if a1 < len(nums1):
                nm1 = nums1[a1]
                nm1_bool = True
            if a2 < len(nums2):
                nm2 = nums2[a2]
                nm2_bool = True
            
            if nm1_bool and nm2_bool:
                if nm1 <= nm2:
                    final_put = nm1
                    a1 += 1
                elif nm1 > nm2:
                    final_put = nm2
                    a2 += 1     
            elif nm1_bool:
                final_put = nm1
                a1 += 1
            elif nm2_bool:
                final_put = nm2
                a2 += 1
            elif nm1_bool == False and nm2_bool == False:
                break

            if final_put >= -1000001 and i in median_idx:
                m += final_put
                
            if median_idx[-1] == i:
                break

        return m / len(median_idx)
                