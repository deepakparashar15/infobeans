"""
4. Reverse a Number
A security system stores OTP codes in reverse format for encryption to increase data safety.
 Reversing a number means extracting digits and rebuilding it in reverse order.
Write a program to **reverse a given integer using loops**.

Input: 1234
Output: 4321



using While loops
n = int(input("Enter NO.: "))

while n != 0:
    print(n % 10, end="")
    n = n // 10
    
"""
    
using for loops
    
    
n = int(input("Enter NO.: "))
rev=0
ans=0 
for i in range(0 , len(str(n))):
    rev=n%10
    ans=ans*10 + rev 
    n = n // 10
         
         
print(ans)
         