1# Definition for singly-linked list.
2# class ListNode(object):
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6
7class Solution(object):
8    def addTwoNumbers(self, l1, l2):
9        # Convert l1 to number considering reversed order
10        number1 = 0
11        place = 1
12        current = l1
13        while current:
14            number1 += current.val * place  # multiply by place
15            place *= 10
16            current = current.next
17
18        # Convert l2 to number considering reversed order
19        number2 = 0
20        place = 1
21        current = l2
22        while current:
23            number2 += current.val * place
24            place *= 10
25            current = current.next
26
27        # Sum the numbers
28        summ = number1 + number2
29
30        # Convert sum to reversed linked list (rookie style)
31        prev = None
32        for digit in str(summ):
33            node = ListNode(int(digit))
34            node.next = prev
35            prev = node
36
37        return prev