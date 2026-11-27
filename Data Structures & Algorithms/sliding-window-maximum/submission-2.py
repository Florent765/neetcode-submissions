class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        deleted = Counter()

        maxHeap = []
        l = 0
        for i in range(k - 1):
            heapq.heappush(maxHeap, -nums[i])

        for r in range(k - 1, len(nums)):
            heapq.heappush(maxHeap, -nums[r])
            while deleted[maxHeap[0]] > 0:
                deleted[maxHeap[0]] -= 1
                heapq.heappop(maxHeap)
            maxW = maxHeap[0]
            res.append(-maxW)
            deleted[-nums[l]] += 1
            l += 1

        return res
