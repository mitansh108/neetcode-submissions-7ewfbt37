class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(x,y):
            return (x**2 + y**2)**0.5
        
        ans_heap = []
       
        for x,y in points:
            d = distance(x,y)
            if len(ans_heap) < k:
                heapq.heappush(ans_heap, (-d, x, y))

            else:
                heapq.heappushpop(ans_heap, (-d, x, y))
        
        return [(x,y) for d, x, y, in ans_heap]