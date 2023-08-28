'''
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def partition_lists(head , x):
    #dummy nodes
    left, right = ListNode(), ListNode()
    #tails to track each partitions
    l_tail, r_tail = left, right

    while head:
        #add to left partition
        if head.val < x:
            l_tail.next = head
            #update pointer
            l_tail = l_tail.next
        #right partition
        else:
            r_tail.next = head
            r_tail = r_tail.next
        head = head.next

    #connect two partitions
    l_tail.next = right.next
    #make sure last node on r_tail is Null
    r_tail.next = None
    return left.next


