1class Solution:
2    def threeSum(self, nums: list[int]) -> list[list[int]]:
3        nums.sort()
4        result = []
5
6        for i in range(len(nums) - 2):
7
8            # Skip duplicate first numbers
9            if i > 0 and nums[i] == nums[i - 1]:
10                continue
11
12            left = i + 1
13            right = len(nums) - 1
14
15            while left < right:
16                total = nums[i] + nums[left] + nums[right]
17
18                if total == 0:
19                    result.append([nums[i], nums[left], nums[right]])
20                    left += 1
21                    right -= 1
22
23                    # Skip duplicates
24                    while left < right and nums[left] == nums[left - 1]:
25                        left += 1
26
27                elif total < 0:
28                    left += 1
29                else:
30                    right -= 1
31
32        return result