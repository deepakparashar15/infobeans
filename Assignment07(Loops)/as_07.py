"""
**7. Count Even Digits**
A data analyst is analyzing numeric IDs and needs to determine how many digits in the ID are even.
Write a program to **count the number of even digits in a given number using loops**.

Input: 123456
Output: Even digits count = 3


n = int(input("Enter NO.: "))                                        

l = len(str(n))
c = 0
i = 0

while i < l:
    a = n % 10

    if a % 2 == 0:
        c += 1

    n = n // 10
    i += 1

print("Even digits count =", c)

"""

using foir loop

n = int(input("Enter NO.: "))                                        

l = len(str(n))
c = 0
i = 0

for i in range(l):
    a = n % 10

    if a % 2 == 0:
        c += 1

    n = n // 10
    i += 1

print("Even digits count =", c)