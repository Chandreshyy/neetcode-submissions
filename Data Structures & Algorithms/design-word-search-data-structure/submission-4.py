class TrieNode:
    def __init__(self) -> None:
        self.children = [None]*26
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
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
        n = len(word)
        
        def backtrack(i, node):
            if not node:
                return False
            if i == n:
                return node.is_end
            char = word[i]
            index = ord(char) - ord('a')
            # print(f"word={word} index={index}, char={char}")
            if char != '.' and not node.children[index]:
                return False
            if char == '.':
                for j in range(26):
                    if node.children[j] and backtrack(i+1, node.children[j]):
                        return True
                return False
            else:
                return backtrack(i+1, node.children[index])
        
        result = backtrack(0, node)
        return result


            

        
