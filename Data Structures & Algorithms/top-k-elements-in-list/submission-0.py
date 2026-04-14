class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Sorting
        hashmap = {}

        for num in nums:
            count = hashmap.get(num, 0)
            count += 1
            hashmap[num] = count

        arr = []
        for num, count in hashmap.items():
            arr.append([count, num])
        arr.sort()

        result = []
        while len(result) < k:
            result.append(arr.pop()[1])

        return result