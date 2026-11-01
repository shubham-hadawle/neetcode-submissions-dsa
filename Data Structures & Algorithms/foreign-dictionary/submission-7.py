class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        hashMap = { char : set() for word in words for char in word }

        for i in range(0, len(words)-1):
            w1, w2 = words[i], words[i+1]

            if len(w2) < len(w1) and w2 == w1[:len(w2)]:
                return ""

            minLength = min(len(w1), len(w2))
            for i in range(0, minLength):
                if w1[i] != w2[i]:
                    hashMap[w1[i]].add(w2[i])
                    break

        visited = {}
        result = []

        def dfs(char):
            if char in visited:
                return visited[char]

            visited[char] = True

            for nei in hashMap[char]:
                if dfs(nei):
                    return True

            visited[char] = False
            result.append(char)

        for char in hashMap:
            flag = dfs(char)
            if flag:
                return ""

        reversed_result = result[::-1]
        return "".join(reversed_result)