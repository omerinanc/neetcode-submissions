class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max = 0
        i=0
        j=len(heights)-1
        while j-i >= 1:
            temp = 0
            if heights[i] <= heights[j]:
                temp = heights[i] * (j-i)
                i +=1
            elif heights[j] <= heights[i]:
                temp = heights[j] * (j-i)
                j-=1
            if temp > max:
                max = temp
            
        return max
        