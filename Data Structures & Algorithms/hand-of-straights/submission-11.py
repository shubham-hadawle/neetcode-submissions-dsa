import heapq

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        hashMap = {}
        for h in hand:
            hashMap[h] = 1 + hashMap.get(h, 0)

        minHeap = list(set(hand))
        heapq.heapify(minHeap)
        result = []

        while minHeap:
            group = []
            first_val = minHeap[0]

            for i in range(first_val, first_val + groupSize):
                if i in hashMap:
                    if hashMap[i] != 0:
                        group.append(i)
                        hashMap[i] -= 1

                    if hashMap[i] == 0:
                        if i != minHeap[0]:
                            return False
                        heapq.heappop(minHeap)
                else:
                    return False

            result.append(group)

        return True