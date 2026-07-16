# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def reverse(node1, node2):
            prev = None
            cur = node1
            while cur != node2:
                cur_next = cur.next
                cur.next = prev
                prev = cur
                cur = cur_next
            return prev, node1

        cur = ListNode()
        res = cur
        cur.next = head
        temp = 1
        temp_node = cur.next
        while temp_node:
            if temp < k:
                print(temp, temp_node.val)
                temp += 1
                temp_node = temp_node.next
            else:
                print('else', k, temp_node.val)
                print('cur.val', cur.val)
                temp_node_next = temp_node.next
                print('input', cur.next.val, temp_node_next.val if temp_node_next else None)
                node1, node2 = reverse(cur.next, temp_node_next)
                print("reversed node", node1.val, node2.val)
                cur.next = node1
                node2.next = temp_node_next
                cur = node2
                temp = 1
                temp_node = temp_node_next
                # break
            
        return res.next


                


