'''
212. Word Search II***
Hard

Given an m x n board of characters and a list of strings words, return all words on the board.
Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Example 1:
Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

Example 2:
Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
'''
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(board, i, j, node, path, result):
            if node.is_end_of_word:
                result.add(path)
                node.is_end_of_word = False #We can mark that a word is completed, so to avoid duplicates. Marking it as false

            if not (0 <= i < len(board)) or not (0 <= j < len(board[0])) or (i, j) in visited or board[i][j] not in node.children:
                return

            visited.add((i, j))
            node = node.children[board[i][j]]
            path += board[i][j]

            for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                dfs(board, x, y, node, path, result)

            visited.remove((i, j))

        trie = Trie()
        for word in words:
            trie.insert(word)

        result = set()
        visited = set()

        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(board, i, j, trie.root, "", result)
    
        return list(result)
        
        