from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # BFS (with Pattern based Adjacency Matrix)
        if endWord not in wordList:
            return 0

        adj = collections.defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                adj[pattern].append(word)

        visited = set()
        dq = deque([beginWord])
        counter = 1

        while dq:
            for n in range(len(dq)):
                word = dq.popleft()

                if word == endWord:
                    return counter

                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:]

                    for neiWord in adj[pattern]:
                        if neiWord not in visited:
                            visited.add(neiWord)
                            dq.append(neiWord)

            counter += 1

        return 0