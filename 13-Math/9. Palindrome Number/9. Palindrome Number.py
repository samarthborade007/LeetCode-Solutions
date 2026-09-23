1class Solution(object):
2    def isPalindrome(self, x):
3        
4        :type x: int
5        :rtype: bool
6        
7        x = str(x)
8        n = len(x)
9        s= 
10        for i in range(n):
11            s += x[-(i+1)]
12        return s == x
13
14
15        