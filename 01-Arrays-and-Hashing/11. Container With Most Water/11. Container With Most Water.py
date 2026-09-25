1class Solution:
2    def maxArea(self, height: list[int]) -> int:
3        left = 0
4        right = len(height) - 1
5        max_area = 0
6
7        while left < right:
8            width = right - left
9            h = min(height[left], height[right])
10
11            area = width * h
12            max_area = max(max_area, area)
13
14            # Move the shorter wall
15            if height[left] < height[right]:
16                left += 1
17            else:
18                right -= 1
19
20        return max_area