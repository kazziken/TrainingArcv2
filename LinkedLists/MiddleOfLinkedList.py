'''

Return middle of linked list

'''

def middle_of_linked_list(self, head):

    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow