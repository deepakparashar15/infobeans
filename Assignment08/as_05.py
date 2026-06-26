"""
5. Count Factors of Number
A mathematics learning app gives practice questions where students 
must know how many factors a number has. The app should automatically
 count the total factors of the entered number.
Write a program to count total factors of a number using loops.

Input:
12

Output:
Factors Count = 6
"""


n1=int(input("ENTER VALUE : "))
c=0
for i in range( 1 ,n1+1):
    if n1 % i ==0:
        c+=1
               
print(c)

