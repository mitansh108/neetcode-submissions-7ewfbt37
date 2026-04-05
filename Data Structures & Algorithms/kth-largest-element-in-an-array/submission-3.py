class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        nums = [-n for n in nums]
        
        heapq.heapify(nums)
        count = 0
        while nums:
            val = heapq.heappop(nums)
            count+=1

            if count == k:
                return -val

        

        

        
        