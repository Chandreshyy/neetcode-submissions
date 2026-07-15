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

        if not lists:
            return None
        
        while len(lists) > 1:
            merge_lists = []

            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i + 1] if i + 1 < len(lists) else None
                merge_lists.append(merge_two_sorted_ll(list1, list2))
            
            lists = merge_lists
        
        return lists[0]

