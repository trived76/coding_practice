'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
'''



'''
Runtime: 202 ms, faster than 5.24% of Python3 online submissions for Add Two Numbers.
Memory Usage: 14.3 MB, less than 15.78% of Python3 online submissions for Add Two Numbers.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans_ = ListNode((l1.val + l2.val) % 10)
        carry_over_ = (l1.val + l2.val) // 10
        ans_list = list()
        ans_list.append(ans_)
        while True:
            if l1.next != None and l2.next != None:
                ans_ = ListNode((l1.next.val + l2.next.val + carry_over_) % 10)
                ans_list.append(ans_)
                carry_over_ = (l1.next.val + l2.next.val + carry_over_) // 10
                l1 = l1.next
                l2 = l2.next
            elif l1.next == None and l2.next != None:
                ans_ = ListNode((l2.next.val + carry_over_) % 10)
                ans_list.append(ans_)
                carry_over_ = (l2.next.val + carry_over_) // 10
                l2 = l2.next
            elif l1.next != None and l2.next == None:
                ans_ = ListNode((l1.next.val + carry_over_) % 10)
                ans_list.append(ans_)
                carry_over_ = (l1.next.val + carry_over_) // 10
                l1 = l1.next
            elif l1.next == None and l2.next == None and carry_over_ == 0:
                break
            else:
                ans_ = ListNode(carry_over_ % 10)
                carry_over_ = (carry_over_) // 10
                ans_list.append(ans_)

        final_ans = ans_list[len(ans_list) -1]
        for ind in range(len(ans_list) - 2 , -1, -1):
            final_ans = ListNode(ans_list[ind].val, final_ans)
        return final_ans