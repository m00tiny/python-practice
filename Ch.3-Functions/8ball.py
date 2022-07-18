#!/usr/bin/env python3
import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain.'
    elif answerNumber == 2:
        return 'It is decidedly so.'
    elif answerNumber == 3:
        return 'Yes.'
    elif answerNumber == 4:
        return 'Reply hazy try again.'
    elif answerNumber == 5:
        return 'Ask again later.'
    elif answerNumber == 6:
        return 'Concentrate and ask again.'
    elif answerNumber == 7:
        return 'Outlook not so good.'
    elif answerNumber == 8:
        return 'Very doubtful.'


input("Ask the magic 8 ball a question.\r\n"),
r = random.randint(1, 8)
print(getAnswer(r))
