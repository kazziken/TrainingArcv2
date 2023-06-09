'''

You are given the head of two sorted linked lists 'list1' and 'list2'

Merge the two lists in a one sorted list.

The list should be made by splicing together the nodes of the first two lists

Return the head of the merged linked list

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

'''

'''
Explanation:

dummy node is created as the starting point of the new merged list.
curr variable is initalized to reference the  
it keeps track of the last node of the merged list,
 which allows appending new nodes

whichever val is lower -
curr.next is the whole list1 or list2 and will keep going.

at the end of the loop curr is pointing to the last node of the merged list 
update curr = curr.next to move along to the next node.

finally return dummy.next to return us the whole merged list

'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_sorted_lists(list1, list2):

    dummy = ListNode()
    curr = dummy

    #breaks after one list is empty
    while list1 and list2:
        if list1.val < list2.val:
            curr.next = list1
            list1 = list1.next
        if list2.val < list1.val:
            curr.next = list2
            list2 = list2.next
        #move to next node
        curr = curr.next
    curr.next = list1 or list2

    return dummy.next