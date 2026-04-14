class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ''
        for string in strs:
            encodedString += str(len(string)) + '#' + string
        print("Encoded String:", encodedString)
        return encodedString

    def decode(self, s: str) -> List[str]:
        decodedResult = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1

            length = int(s[i:j])   # Numbers in the position i to j, but not including j.
            # The number may be a 2 or 3 digit number, hence we use s[i:j]
            i = j+1 + length

            decodedString = str(s[j+1 : j+1+length])
            decodedResult.append(decodedString)

        return decodedResult