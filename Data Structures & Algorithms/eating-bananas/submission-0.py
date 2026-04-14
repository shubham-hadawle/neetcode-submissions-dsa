class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # # Brute Force
        # maxValueInPiles = max(piles)
        # print(maxValueInPiles)

        # for k in range(1, maxValueInPiles+1):
        #     hours = 0
        #     for p in piles:
        #         hours += math.ceil(p/k)

        #     if hours <= h:
        #         return k

        # Binary Search
        l, r = 1, max(piles)
        result = r      # NOTE: the max value is definitely the result

        while l <= r:
            k = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)

            if hours <= h:
                result = min(result, k)
                r = k - 1
            elif hours > h:
                l = k + 1

        return result

