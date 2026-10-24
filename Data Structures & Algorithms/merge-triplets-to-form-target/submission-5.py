class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        result = set()

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue

            for idx, val in enumerate(t):
                if val == target[idx]:
                    result.add(idx)

        if len(result) == 3:
            return True
        return False