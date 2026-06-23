'''
14. Online Course Fee System

An online platform offers courses with fixed fees:

* Programming → ₹5000
* Design → ₹4000
* Marketing → ₹3000
  Discount is applied based on user type:
* Student → 20% discount
* Working Professional → 10% discount
* Others → No discount

Write a Python program to calculate final course fee.

Input:
Enter course category: Programming
Enter user type: Student

Output:
Final Course Fee: ₹4000
'''

course = input("Enter course category: ")
user = input("Enter user type: ")

if course == "Programming":
    fee = 5000

elif course == "Design":
    fee = 4000
else:
    fee = 3000
if user == "Student":
    discount = fee * 20 / 100

elif user == "Working Professional":
    discount = fee * 10 / 100
else:
    discount = 0
final_fee = fee - discount

print("Final Course Fee: ₹", final_fee)