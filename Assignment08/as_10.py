"""
10. Student ID Validity Checker (Count Odd Digits)
A school management system assigns numeric IDs to students. The administration wants to verify IDs by checking how many odd digits are present in each ID number. IDs with more odd digits are sent for manual review.

Write a program to count the number of odd digits in a given student ID using loops.

Input:
572943

Output:
Odd Digits Count = 3

using while loop

n=int(input("ENTER VALUE : "))
c=0
while n>0:
    a=n%10
    if a % 2 ==1:
        c+=1
    n//=10           
print(c)


"""
using for loop

n=int(input("ENTER VALUE : "))
c=0
for i in range(len(str(n))):
    a=n%10
    if a % 2 ==1:
        c+=1
    n//=10           
print(c)
