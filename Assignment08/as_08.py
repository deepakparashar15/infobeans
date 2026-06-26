"""

8. Count Multiples of 5 Between Two Numbers
A supermarket gives coupons to customers whose token numbers are multiples of 5. 
The manager enters a token range and wants to know how many eligible token numbers exist.
Write a program to count numbers divisible by 5 between two given numbers using loops.

Input:
1 20

Output:
Count = 4

uusing for loop


n1=int(input("ENTER VALUE : "))
n2=int(input("ENTER VALUE : "))
c=0
for i in range(n1 , n2+1):
    if i %5==0:
	    c+=1
	    
print(c)
"""
using while loop

n1=int(input("ENTER VALUE : "))
n2=int(input("ENTER VALUE : "))
c=0
while n1 <=n2:
    if n1 %5==0:
	    c+=1
    n1+=1    
print(c)

