class TrieNode:

    def __init__(self) -> None:
        self.children = [None] * 26
        self.is_end = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            index = ord(char) - ord('a')
            if not node.children[index]:
                new_node = TrieNode()
                node.children[index] = new_node
            node = node.children[index]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            index = ord(char) - ord('a')
            if not node.children[index]:
                return False
            node = node.children[index]
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            index = ord(char) - ord('a')
            if not node.children[index]:
                return False
            node = node.children[index]
        return True
        
        