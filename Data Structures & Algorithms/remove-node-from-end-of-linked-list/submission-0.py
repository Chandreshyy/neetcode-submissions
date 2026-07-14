# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        cur = ListNode()
        cur.next = head
        head = cur
        nth = cur

        while n > 0:
            nth = nth.next
            n = n - 1

        while nth.next:
            nth = nth.next
            cur = cur.next
        
        cur.next = cur.next.next

        return head.next

        
