# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head

        while curr and curr.next:
            first = curr
            second = curr.next

            # Performing swap
            prev.next = second
            first.next = second.next
            second.next = first

            # Repositioning pointers for next iteration
            prev = first
            curr = first.next

        return dummy.next