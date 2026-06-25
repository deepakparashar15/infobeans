
"""
**8. Count Odd Digits**
A banking system flags IDs with too many odd digits for further verification.
Write a program to **count the number of odd digits in a given number using loops**.

Input: 123456
Output: Odd digits count = 3

"""


n = int(input("Enter NO.: "))                                        

l = len(str(n))
c = 0
i = 0

while i < l:
    a = n % 10

    if a % 2 == 1:
        c += 1

    n = n // 10
    i += 1

print("Even digits count =", c)

n = int(input("Enter NO.: "))                                        

"""

using for loops

l = len(str(n))
c = 0
i = 0

for i in range(l):
    a = n % 10

    if a % 2 == 1:
        c += 1

    n = n // 10
    i += 1

print("Even digits count =", c)
"""