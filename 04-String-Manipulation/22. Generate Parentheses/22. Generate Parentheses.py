1class Solution(object):
2    def generateParenthesis(self, n):
3        res = []
4        def backtrack(s, open_count, close_count):
5            if len(s) == 2 * n:
6                res.append(s)
7                return
8            if open_count < n:
9                backtrack(s + (, open_count + 1, close_count)
10            if close_count < open_count:
11                backtrack(s + ), open_count, close_count + 1)
12        backtrack(, 0, 0)
13        return res
14