class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        max_water = 0

        i = 0
        j = len(heights)-1

        while i < j:
            water = (j-i) * min(heights[i], heights[j])
        
            if water > max_water:
                max_water = water

            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1

        return max_water