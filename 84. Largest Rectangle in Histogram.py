Question:
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return 
the area of the largest rectangle in the histogram.








Solution: (similar to 496.)
  
  Monotonic stack
  
  for more explanation: read pdf: Largest Rectangle In Histogram.pdf
  
  
class Solution(object):
    def largestRectangleArea(self, heights):

        stack = [-1]
        heights.append(0)
        ans = 0
        for i, height in enumerate(heights):
            while heights[stack[-1]] > height:
                h = heights[stack.pop()] 
                w = i - stack[-1] - 1
                ans = max(ans, h*w)
            stack.append(i)
        heights.pop()
        return ans  
