class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        c = Counter(hand)
        minHeap = list(c.keys())
        heapq.heapify(minHeap)

        while minHeap:
            first = minHeap[0]

            for i in range(first, first + groupSize):
                if i not in c:
                    return False
                c[i] -= 1
                if c[i] == 0:
                    if i != minHeap[0]:
                        return False
                    heapq.heappop(minHeap)
        
        return True