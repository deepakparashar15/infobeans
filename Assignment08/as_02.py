"""
2. Smallest Digit in Number
A manufacturing company prints serial numbers on products. During quality testing, the scanner needs to detect the smallest digit in the serial number to verify coding standards.
Write a program to find the smallest digit in a number using loops.

Input:
57294

Output:
Smallest Digit = 2

"""

n=int(input("ENTER VALUE : "))
min=n
while n>0:
    a=n%10
	
    if min > a:
        min=a
    n//=10
print(min)