# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        def reverse_ll(head):
            prev = None
            cur = head
            while cur:
                nextt = cur.next
                cur.next = prev
                prev = cur
                cur = nextt
            
            return prev
    
        cur = head
        slow = cur
        fast = cur

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # print(slow.val)
        # if fast:
        #     print(fast.val)
        nextt = slow.next
        slow.next = None
        reverse_slow = reverse_ll(nextt)
        # print(reverse_slow.val)
        print(cur.val)
        new_ll = ListNode()
        temp = new_ll
        while cur and reverse_slow:
            temp.next = cur
            cur = cur.next
            temp = temp.next
            temp.next = reverse_slow
            reverse_slow = reverse_slow.next
            temp = temp.next

        # print(reverse_slow.val)
        print(cur.val)
        while cur:
            temp.next = cur
            cur = cur.next
            temp = temp.next
        while reverse_slow:
            temp.next = reverse_slow
            reverse_slow = reverse_slow.next
            temp = temp.next
        
        head = new_ll.next
