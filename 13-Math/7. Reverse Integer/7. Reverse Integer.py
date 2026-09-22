1class Solution(object):
2    def reverse(self, x):
3        
4        :type x: int
5        :rtype: int
6        
7        x_str = str(x)
8        if x_str[0] == -:
9            x_str1 = x_str.replace('-', '')
10        else:
11            x_str1 = x_str
12
13        n = len(x_str1)
14        rev = 
15        rev_list = []
16        for i in range(n):
17            rev_list.append(x_str1[-(i+1)])
18        # print(rev_list)
19
20        for i in rev_list:
21            rev += i
22
23        rev_n = int(rev)
24        if x < 0:
25            rev_n = -rev_n
26
27        # *** 32-bit signed integer check ***
28        if rev_n < -2**31 or rev_n > 2**31 - 1:
29            return 0
30
31        return rev_n
32