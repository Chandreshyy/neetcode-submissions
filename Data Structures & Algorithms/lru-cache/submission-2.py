
class DoubleListNode:
    def __init__(self, key=0, val=0, next=None, prev=None) -> None:
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.mapp = {}
        self.capacity = capacity
        self.head = DoubleListNode()
        self.tail = DoubleListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        node_next = node.next
        node_prev = node.prev
        node_next.prev = node_prev
        node_prev.next = node_next
        node.next = None
        node.prev = None
    
    def add_new_node(self, node):
        head_nextt = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = head_nextt
        head_nextt.prev = node

    def get(self, key: int) -> int:
        if key in self.mapp:
            self.remove(self.mapp[key])
            self.add_new_node(self.mapp[key])
            return self.mapp[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.mapp:
            self.mapp[key].val = value
            self.remove(self.mapp[key])
            self.add_new_node(self.mapp[key])
        else:
            new_node = DoubleListNode(key=key, val=value)
            self.add_new_node(new_node)
            self.mapp[key] = new_node
            if len(self.mapp) > self.capacity:
                last_node = self.tail.prev
                last_key = last_node.key
                self.remove(last_node)
                self.mapp.pop(last_key)








        
