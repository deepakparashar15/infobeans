"""
6. Armstrong Number (3-digit)
In coding competitions, certain numbers are considered unique. 
A 3-digit Armstrong number is one where the sum of the cubes of its digits equals the number itself.
Write a program to **check whether a number is an Armstrong number using loops**.

Input: 153
Output: Armstrong

using while loop

n = int(input("Enter NO.: "))
n1=n
l=len(str(n))
s=0
a=0
while n != 0:
    a=n % 10    
    m=1
    i=0  
    while i < l:
        m=a*m
        i+=1    
    
    s=s+m
    n//=10   

if n1==s:
    print("NO IS AMSTRONG" , s)
else:
    print("NO IS NOT AMSTRONG" , s)
      
"""


