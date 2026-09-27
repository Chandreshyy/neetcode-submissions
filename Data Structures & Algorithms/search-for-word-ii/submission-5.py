class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.word = None

class Solution:
    def __init__(self) -> None:
        self.root = TrieNode()
    
    def add_word(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                new_node = TrieNode()
                node.children[char] = new_node
            node = node.children[char]
        node.word = word

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        for word in words:
            self.add_word(word)

        result = []
        rows = len(board)
        cols = len(board[0])
        res_set = set()

        def backtrack(row, col, node):
            if node.word and node.word not in res_set:
                result.append(node.word)
                res_set.add(node.word)
            if row < 0 or col < 0 or row >= rows or col >= cols:
                return
            old_char = board[row][col]
            
            if old_char == '#' or old_char not in node.children:
                return
            board[row][col] = '#'
            backtrack(row+1, col, node.children[old_char])
            backtrack(row-1, col, node.children[old_char])
            backtrack(row, col+1, node.children[old_char])
            backtrack(row, col-1, node.children[old_char])
            board[row][col] = old_char
        
        for i in range(rows):
            for j in range(cols):
                backtrack(i, j, self.root)
        return result
            
        

        
        