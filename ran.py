import random

thenumber = random.randint(0,100)

while True:
 guess = int(input("Guess a number from 0 to 100! "))
 if input == thenumber:
    print("Correct")
    break
 elif thenumber < guess:
     print("Too big!")
 elif thenumber > guess:
     print("Too small")