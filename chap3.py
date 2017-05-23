# def spam():
#   eggs = 99
#   bacon()
#   print(eggs)

# def bacon():
#   ham = 101
#   eggs = 0

# spam()

#########
# def spam():
#     print(eggs)
# eggs = 42
# spam()
# print(eggs)

############
# def spam():
#   eggs = 'spam local'
#   print(eggs) # prints 'spam local'

# def bacon():
#   eggs = 'bacon local'
#   print(eggs) # prints 'bacon local'
#   spam()
#   print(eggs) # prints 'bacon local'

# eggs = 'global'
# bacon()
# print(eggs) # prints 'global'

# ######################
# def spam():
#   print(eggs)

# def bacon():
#   eggs = 'bacon' # this is a local

# def ham():
#   print(eggs) # this is the global

# eggs = 42 # this is the global
# spam()
# print(eggs)

#####################
# def spam():
#   print(eggs) # ERROR!
#   eggs = 'spam local'

# eggs = 'global'
# spam()

##########
# def spam():
#   try:
#     print(eggs) # ERROR!
#     eggs = 'spam local'

#   except UnboundLocalError:
#     print('The Egg varibale must be declared within the funcion and before its use or a call to a global variable with the same name should be made')

# eggs = 'global'
# spam()

########################
# def spam(divideBy):
#     return 42 / divideBy

# print(spam(2))
# print(spam(12))
# print(spam(0))
# print(spam(1))

#################
# def spam(divideBy):
#     try:
#         return 42 / divideBy
#     except ZeroDivisionError:
#         print('Error: Invalid argument.')

# print(spam(2))
# print(spam(12))
# print(spam(0))
# print(spam(1))

############
# # Guess the number game
# import random
# import titlecase


# print('Hi, what is your name?:')
# name = input()

# print('')
# print('Hi ' + name)
# print('I am thinking of a number between 1 and 20.')

# number = random.randint(1,20)

# #As the user to guess 6 times
# numberOfGuesses = 1
# while numberOfGuesses < 7:
#   print('Take a guess:')
#   guess = int(input())

#   if guess > number:
#     print('Your guess is too high.')
#     print('')
#   elif guess < number:
#     print('Your guess is too low.')
#     print('')
#   else:
#     break
#   numberOfGuesses = numberOfGuesses + 1

# if number == guess:
#   print('Good job! You guessed my number in ' + str(numberOfGuesses) + ' guesses!')
# else:
#   print('Nope. The number I was thinking of was ' + str(number))

##############
def collatz(number):
  while number != 1:
    if number == 1:
      break

    elif number % 2 == 1:
      print(3 * number + 1)
      number = 3 * number + 1

    elif number % 2 == 0:
      print(number // 2)
      number = number // 2

while True:
  try:
    print('Enter a number:')
    number = int(input())
    number = collatz(number)

  except ValueError:
    print('Value entered was not an interger')