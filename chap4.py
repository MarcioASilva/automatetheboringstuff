# spam = []
# spam.sort()
# print(spam)
# spam.sort(reverse=True)

# ham = ['Alice', 'alice', 'Bob', 'bob', 'Carol', 'carol']

# ham.sort(key=str.lower)
# print(ham)

################
# This is a guess the number game
#Importing ramdom package
# import random
# messages = [  'It is certain',
#               'It is decidedly so',
#               'Yes definitely',
#               'Reply hazy try again',
#               'Ask again later',
#               'Concentrate and ask again',
#               'My reply is no',
#               'Outlook not so good',
#               'Very doubtful'
#             ]

# print(messages[random.randint(0, len(messages) - 1)])

# supplies = ['pens','staplers','flame throwers','binders']
# for i in range(len(supplies)):
#   print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

# cat = ['fat','orange','loud']
# size, colour, disposition = cat

# print(size)
# print(colour)
# print(disposition)

# a = 'AAA'
# b = 'BBB'

# a, b = b,a
# print(a)
# print(b)

# spam = 1
# spam +=1
# print(spam)

# def eggs(someParameter):
#     someParameter.append('Hello')

# spam = [1, 2, 3]
# eggs(spam)
# print(spam)

# def eggs(someParameter):
#     someParameter = someParameter + 1
#     return someParameter

# spam = 1
# eggs(spam)
# print(spam)

# import copy
# spam = ['A', 'B', 'C', 'D']
# cheese = copy.copy(spam)

# cheese[1] = 42
# print(spam)
# print(cheese)

# import copy
# eggs = [[1,2,6],['a','b','c'],['x','y','z']]
# cheese = copy.deepcopy(eggs)
# cheese[0][0] = 0
# print(cheese)
# print(eggs)

# spam2 = [2, 4, 6, 8, 10]
# spam2[2] = 'hello'
# print(spam2)

# spam3 = ['a', 'b', 'c', 'd']
# spam3 = spam3 + spam3
# print(spam3)
# print(spam3[int(int('3' * 2) // 11)])

###############
# #Comma Code
# spam = ['apples', 'bananas', 'tofu', 'cats']

# def conc(list):
#   concat = ''

  # for i in list:
  #   if i != list[-1]:
  #     concat = concat + str(i) + ", "
  #   else:
  #     concat = concat + "and " + str(i)
  # return concat

# result = conc(spam)
# print(result)

#Character Picture Grid
grid = [  ['.', '.', '.', '.', '.', '.'],
          ['.', 'O', 'O', '.', '.', '.'],
          ['O', 'O', 'O', 'O', '.', '.'],
          ['O', 'O', 'O', 'O', 'O', '.'],
          ['.', 'O', 'O', 'O', 'O', 'O'],
          ['O', 'O', 'O', 'O', 'O', '.'],
          ['O', 'O', 'O', 'O', '.', '.'],
          ['.', 'O', 'O', '.', '.', '.'],
          ['.', '.', '.', '.', '.', '.']
        ]

string = ''
for j in range(0,len(grid[0])):#Evaluates to 6 (Horizontal)
  for i in range(0,len(grid)): #Evaluates to 9 (Vertical)
    if j == 0:
      string = string + grid[i][j]
    else:
      string = string + grid[i][j]

  string = string + ('\n')
print(string)






