"""
*9. Check All Digits Are Even**
A machine only accepts numbers where every digit is even. If any digit is odd, the number is rejected.
Write a program to **check whether all digits of a number are even using loops**.

Input: 2468
Output: All Even

Input: 2456
Output: Not All Even

using fopr loop
"""
 
n = int(input("Enter NO.: "))                                        

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

'''



n=int(input("Enter The Number : "))
sum=0

while n>0:
    a=n%10
    sum+=a
    n//=10
   
print("All Even" if sum%2==0 else "Not All Even")