"""
1. Sum of First N Natural Numbers
A teacher wants to reward students by giving points daily.
On day 1, a student gets 1 point, day 2 → 2 points, and so on. This follows a natural number sequence.
Write a program to calculate the **total points earned after n days** 
by summing all natural numbers up to n using loops.

Input: n = 10
Output: Total Points = 55

"""

For loops

n=int(input("Enter NO.: "))
s=0
for i in range(n+1):
   s=s+i
print( "Total Points = " ,s) 


using While loop

n=int(input("Enter NO.: "))
s=0
i=0
while i<=n:
   s=s+i 
   i+=1
   
print(" Total Points = " ,s)   

