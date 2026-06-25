"""
5. Palindrome Check
A number plate is considered special if it reads the same forward and backward. Such numbers are called palindromes.
Write a program to **check whether a given number is a palindrome using loops**.

Input: 121
Output: Palindrome


using While  loops

n = int(input("Enter NO.: "))
temp=n
a=0
while n!=0:
   a=(n%10) + a*10
   n=n//10
   
if temp == a:
   print("NO. IS PALINDROME")
else:
   print("NO. IS  not PALINDROME") 
     

     
n = int(input("Enter NO.: "))
temp=n
a=0
s=0
while n!=0:
   a=n%10
   s=s*10 + a
   n=n//10
   
if temp == s:
   print("NO. IS PALINDROME")
else:
   print("NO. IS  not PALINDROME") 
     
""" 

using for loop  
  
  
n = int(input("Enter NO.: "))
temp=n
a=0
s=0 
for i in range(0 , len(str(n))):
    a=n%10
    s=s*10 + a
    n=n//10
   
   
if temp == s:
   print("NO. IS PALINDROME")
else:
   print("NO. IS  not PALINDROME") 
        