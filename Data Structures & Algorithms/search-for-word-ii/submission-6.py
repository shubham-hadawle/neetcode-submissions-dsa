class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

    def addWord(self, word):
        curr = self
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.endOfWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.root = TrieNode()
        for w in words:
            self.root.addWord(w)

        rows, cols = len(board), len(board[0])
        result, visited = set(), set()


        def dfs(r, c, node, formingWord):

            if (r < 0 or c < 0 or r >= rows or c >= cols or 
                (r, c) in visited or board[r][c] not in node.children):
                return

            visited.add((r, c))
            formingWord += board[r][c]
            if node.children[board[r][c]].endOfWord == True:
                result.add(formingWord)
            
            dfs(r+1, c, node.children[board[r][c]], formingWord)
            dfs(r, c+1, node.children[board[r][c]], formingWord)
            dfs(r-1, c, node.children[board[r][c]], formingWord)
            dfs(r, c-1, node.children[board[r][c]], formingWord)
            visited.remove((r, c))

        for r in range(0, rows):
            for c in range(0, cols):
                dfs(r, c, self.root, "")

        return list(result)
