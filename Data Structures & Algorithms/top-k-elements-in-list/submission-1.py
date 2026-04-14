class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # # Sorting
        # hashmap = {}

        # for num in nums:
        #     count = hashmap.get(num, 0)
        #     count += 1
        #     hashmap[num] = count

        # arr = []
        # for num, count in hashmap.items():
        #     arr.append([count, num])
        # arr.sort()

        # result = []
        # while len(result) < k:
        #     result.append(arr.pop()[1])
        # return result


        # Bucket Sort
        hashmap = {}
        for num in nums:
            count = hashmap.get(num, 0) + 1
            hashmap[num] = count

        bucket = [[] for i in range (0, len(nums)+1)]
        for num, count in hashmap.items():
            bucket[count].append(num)

        result = []
        for i in range(len(bucket)-1, 0, -1):
            for num in bucket[i]:
                if len(result) != k and num != []:
                    result.append(num)
        return result