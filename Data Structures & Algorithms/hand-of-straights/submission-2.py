import heapq

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        # Creating a HashMap with cards/numbers as the keys & frquencies as the values.
        hashMap = {}
        for n in hand:
            hashMap[n] = 1 + hashMap.get(n, 0)

        minHeap = list(hashMap.keys())
        heapq.heapify(minHeap)

        while minHeap:
            first_val = minHeap[0]  # minHeap[0] gives the minimum value of the MinHeap without popping

            for i in range(first_val, first_val + groupSize): # Range: first_val to first_val + groupSize - 1
                if (i not in hashMap) or (hashMap[i] == 0):
                    return False
                
                hashMap[i] -= 1

                if hashMap[i] == 0:
                    if i != minHeap[0]:
                        return False

                    heapq.heappop(minHeap)

        return True