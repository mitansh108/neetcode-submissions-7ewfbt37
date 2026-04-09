class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_area = 0

        for i in range(len(heights)):
            area = abs((l-r) * min(heights[l], heights[r]))

            if heights[l] > heights[r]:
                r-=1
            else:
                l+=1
            
            max_area = max(max_area, area)
        return max_area
            

        