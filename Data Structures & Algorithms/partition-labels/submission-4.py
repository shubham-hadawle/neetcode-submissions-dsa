class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashMap = {}
        for index, char in enumerate(s):
            hashMap[char] = index
            # This will automatically ensure that the last occurrrence is updated for every character.

        result = []
        size, end = 0, 0

        for index, char in enumerate(s):
            size += 1
            # Update end the character's last occurence.
            # end = max(end, hashMap[char])
            if end < hashMap[char]:
                end = hashMap[char]

            if index == end:
                result.append(size)
                size = 0

        return result