# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def merge_two_sorted_ll(l1, l2):
            dummy = ListNode()
            head = dummy
            while l1 and l2:
                if l1.val <= l2.val:
                    dummy.next = l1
                    l1 = l1.next
                    dummy = dummy.next
                else:
                    dummy.next = l2
                    l2 = l2.next
                    dummy = dummy.next
            while l1 or l2:
                if l1:
                    dummy.next = l1
                    l1 = l1.next
                    dummy = dummy.next
                if l2:
                    dummy.next = l2
                    l2 = l2.next
                    dummy = dummy.next
            
            return head.next

        n = len(lists)
        if n == 0:
            return None
        if n==1:
            return lists[0]
        res = lists[0]
        for i in range(1, n):
            res = merge_two_sorted_ll(res, lists[i])
        
        return res
