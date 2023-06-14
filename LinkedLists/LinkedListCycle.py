'''
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

'''

'''

Explanation:
Floyd's cycle-finding algorithm, also known as the "fast and slow pointers" technique. 

First assign both fast and slow at the beginning of the linked list,

we want the fast to go two indices forward and slow to go one index forward

and we want to do this while fast is within bounds (not None) so our loop only runs from

while fast and fast.next

If the linked list contains a cycle, the fast pointer will eventually catch up to the slow pointer, resulting in an equality check. 
If no cycle is present, the fast pointer will reach the end of the list (None) before the slow pointer, and the loop will terminate without finding a cycle.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def list_cycle(head):

    fast = slow = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
    return False
