'''
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):

        dummy = ListNode()
        cur_pointer = dummy

        carry = 0
        while l1 or l2 or carry:
            # make sure to add by 0 if 1 list is longer
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # new digit
            val = v1 + v2 + carry

            # say the sum of l1+l2 = 10+
            carry = val // 10
            #so we can make sure its 1 digit
            val = val % 10
            cur_pointer.next = ListNode(val)

            #update pointer
            cur_pointer = cur_pointer.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next