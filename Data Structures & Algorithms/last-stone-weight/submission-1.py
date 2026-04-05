class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [ -s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            first = abs(first)
            second = heapq.heappop(stones)
            second = abs(second)

            if first != second:
                heapq.heappush(stones, second-first)
        
        if not stones:
            return 0
        return abs(stones[0])
        