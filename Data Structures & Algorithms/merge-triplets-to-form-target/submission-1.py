class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue

            for index, value in enumerate(t):
                if value == target[index]:
                    good.add(index)
                    # Adding the 'index' of the triplets to the Set ensures that at most 3 values are stored in the Set.
                    # This allows use to merge as many triplets as required, but still ensure that len(good) does not exceed 3.

        if len(good) == 3:
            return True
        else:
            return False