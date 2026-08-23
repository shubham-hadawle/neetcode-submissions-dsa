class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sorting based on start-time
        intervals.sort(key = lambda x : x[0])

        merged_result = [intervals[0]]   # Adding first interval to the result

        for i in intervals[1:]:
            start, end = i[0], i[1]
            lastEnd = merged_result[-1][1]     # Last end in the merge_result

            if start <= lastEnd:        # Overlapping Intervals
                merged_result[-1][1] = max(lastEnd, end)
            else:                       # No overlap
                merged_result.append(i)

        return merged_result