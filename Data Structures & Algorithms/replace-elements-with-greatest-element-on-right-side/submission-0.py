class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maximum = -1

        for i in range(len(arr)-1, -1, -1):
            temp = arr[i]
            arr[i] = maximum
            maximum = max(maximum, temp)

        return arr