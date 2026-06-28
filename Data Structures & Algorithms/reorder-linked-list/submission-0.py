# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:\
        
        #step 1: find middle (fast and slow pointer)
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        #step 2. set second to the first of the second half and reverse that half
        second = slow.next
        slow.next = None
        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt

        #step 3. zip the two halfes alternatively
        first = head
        second = prev
        while second:
            fnxt = first.next
            snxt = second.next
            first.next = second
            second.next = fnxt
            first = fnxt
            second = snxt

                
        