'''
Given the head of a singly linked list, reverse the list, and return the reversed list.

Input head = [1,2,3,4,5]
output : [5,4,3,2,1]
'''

'''
Explanation:

Can think of it as a two pointer q to make it easier to visualize:

first: save the next so we can traverse through the whole list
then point curr.next towards previous node. Your work is done.

Move the two pointers to continue
prev = curr
curr = temp

'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reversed_linked_list(self, head):

    prev = None
    current = head

    while current:
        temp = current.next
        current.next = prev

        #move to the next iteration
        prev = current
        current = temp
    return prev