from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # # BFS using Deque (with 'abcdefghijklmnopqrstuvwxyz')
        # if endWord not in wordList:
        #     return 0

        # wordList = set(wordList)
        # dq = deque()
        # dq.append([beginWord, 1])

        # while dq:
        #     word, counter = dq.popleft()

        #     if word == endWord:
        #         return counter

        #     for i in range(len(word)):
        #         for char in "abcdefghijklmnoprstuvwxyz":
        #             next_word = word[:i] + char + word[i+1:]
        #             if next_word in wordList:
        #                 dq.append([next_word, counter+1])
        #                 wordList.remove(next_word)

        # return 0
        
        
        # BFS using Deque (with Pattern based Adjacency Matrix)
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