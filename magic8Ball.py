import random
def getAnswer(answerNumber):
  messages = ['It is certain',
              'It is decidedly so',
              'Yes definitely',
              'Reply hazy try again',
              'Ask again later',
              'Concentrate and ask again',
              'My reply is no',
              'Outlook not so good',
              'Very doubtful'
              ]

r = random.randint(1, 9)
fortune = getAnswer(messages[r])
print(fortune)