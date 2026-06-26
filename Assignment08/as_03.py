"""
3. First Digit of Number
A university receives thousands of application IDs. 
The first digit of each ID represents the department code, 
so the admission software must read the first digit quickly.
Write a program to find the first digit of a number using loops.

Input:
53892

Output:
First Digit = 5
"""

n=int(input("ENTER VALUE : "))
a=0
while n>0:
    a=n%10
    n=n//10
print(a)