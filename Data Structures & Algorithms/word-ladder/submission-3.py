class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        hashMap = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(0, len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                hashMap[pattern].append(word)

        visited = set()
        dq = collections.deque()
        dq.append(beginWord)
        visited.add(beginWord)
        counter = 1

        while dq:
            for i in range(0, len(dq)):
                word = dq.popleft()

                if word == endWord:
                    return counter

                for i in range(0, len(word)):
                    pattern = word[:i] + "*" + word[i+1:]

                    for nei in hashMap[pattern]:
                        if nei not in visited:
                            visited.add(nei)
                            dq.append(nei)

            counter += 1

        return 0