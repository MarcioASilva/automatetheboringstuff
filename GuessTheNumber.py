# This is a guess the number game
#Importing ramdom package
import random

#Assignings ramdom value from 1 to 20 to variable secretNumber
secreteNumber = random.randint(1,20)
print("Guess a number between 1 and 20:")

# Ask the player to guess 6 times
for guessTaken in range(1,7):
  print ("Take a guess:")
  guess = int(input())

  if guess < secreteNumber:
    print("Your guess was too low")
  elif guess > secreteNumber:
    print("Your guess was too high")
  else:
    break    # This condition is the correct guess!

#Testing for correct guess
if guess == secreteNumber:
  print("Good job, " + str(guess) + " was the correct number.")
else:
  print("Nooooo, the correct number was " + str(guess) + ".")