
"""
9. Neon Number LED Unlock Game
You're programming a new LED display game. The game level unlocks only when a neon number is entered.

A neon number is a number where the sum of the digits of its square is equal to the number itself.
Example: 9 → 9² = 81 → 8 + 1 = 9

Accept a number from the player.
Check whether it is a neon number using loops.

If true, display:
Glowing Success! You've found the Neon Number!

Otherwise display:
Try again! Not quite glowing yet.

Input:
9

Output:
Glowing Success! You've found the Neon Number!

using whilee loop

n1=int(input("ENTER VALUE : "))
sq=n1**2
s=0
while sq>0:
    a=sq%10
    s=s+a
    sq=sq//10
	
if s == n1:
    print( "Glowing Success! You've found the Neon Number!")
    
else:	
    print("Try again! Not quite glowing yet.")

"""	

using for loop

    
n1=int(input("ENTER VALUE : "))
sq=n1**2
s=0
for i in range(len(str(sq))):
    a=sq%10
    s=s+a
    sq=sq//10
	
if s == n1:
    print( "Glowing Success! You've found the Neon Number!")
    
else:	
    print("Try again! Not quite glowing yet.")

	   