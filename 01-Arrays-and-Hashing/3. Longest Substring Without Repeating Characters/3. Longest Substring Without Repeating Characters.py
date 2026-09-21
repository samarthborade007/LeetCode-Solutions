1class Solution(object):
2    def lengthOfLongestSubstring(self, s):
3        
4        :type s: str
5        :rtype: int
6        
7        max_length = 0
8        n = len(s)
9        for i in range(n):
10            seen = set()
11            length = 0
12            for j in range(i, n):
13                if s[j] in seen:
14                    break   # stop as soon as we hit a duplicate
15                seen.add(s[j])
16                length += 1
17            max_length = max(max_length, length)
18            if n - i <= max_length:
19                break
20
21        return max_length
22