class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Greedy Approach
        result = []

        for curr in range(0, len(intervals)):
            # CASE 1: 'newInterval' falls before 'currInterval'
            if newInterval[1] < intervals[curr][0]:
                result.append(newInterval)
                result = result + intervals[curr:]
                return result

            # CASE 2: 'newInterval' falls after 'currInterval'
            elif intervals[curr][1] < newInterval[0]:
                result.append(intervals[curr])

            # CASE 3: Both overlap
            else:
                newInterval[0] = min(newInterval[0], intervals[curr][0])
                newInterval[1] = max(newInterval[1], intervals[curr][1])

        # CASE 4: 'newInterval' falls/ends after all iterated intervals
        # i.e. the earlier return statement was never executed
        result.append(newInterval)
        return result