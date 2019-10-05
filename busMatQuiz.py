#! python3
#busMatQuiz.py is a quiz program for first year university business math courses

import time, random
mainMenuChoice = int(0)
subMenuChoice = int(00)
#principal, rate, time, interest = 0, 0, 0, 0

def menu(optionAlign, leftWidth, rightWidth):
    for k, v in optionAlign.items():
        print(str(v).ljust(leftWidth, '_') + k.rjust(rightWidth, '_'))
    #print('\n')

def simpleInterestMenu(optionAlign, leftWidth, rightWidth):
    for k, v in optionAlign.items():
        print(str(v).ljust(leftWidth, '_') + k.rjust(rightWidth, '_'))
        #print('\n')

def simPrin():
    principal = random.randint(1, 100)
    return principal

def simRate():
    rate = round(float(random.randint(1, 100)), 2)
    return rate

def simTime():
    time = random.randint(1, 240)
    return time

def simInterest():
    interest = float(random.randint(1, 100))
    return interest

def correctResult(answer, sign1, unit, sign2):
    print('You are correct! The answer is ' + sign1 + '{:.2f}'.format(answer) + unit + sign2)
    simpleInterestMenu(simpleIntOptions, 20, 20)
    subMenuChoice = int(input('\nWhat type of question do you want to practice with? '))

def wrongResult(answer, sign1, unit, sign2):
    print('No, unfortunately the answer is ' + sign1 + '{:,.2f}'.format(answer) + unit + sign2)
    simpleInterestMenu(simpleIntOptions, 20, 20)
    subMenuChoice = int(input('\nWhat type of questions do you want to practice with? '))

def findSimInterest(principal, rate, time):          #Function to find the simple interest
    answer = round(float(principal * rate / 100 * time / 12), 2)
    guess = float(input('What is the interest earned on ${:,.2f} for '.format(principal) + str(time) +
                        ' months at {:.2f}%? '.format(rate)))
    if guess == float(answer):
        correctResult(answer, '$', '', '')
    else:
        wrongResult(answer, '$', '', '')

def findSimPrincipal(rate, time, interest):
    answer = round(float(interest / (rate / 100) * (time / 12)), 2)
    guess = float(input('What is the principal if ${0:,.2f} is earned at {1:.2f}% interest for '.format(interest, rate)
                        + str(time) + ' months.'))
    if guess == float(answer):
        correctResult(answer, '$', '', '')
    else:
        wrongResult(answer, '$', '', '')

def findSimTime(principal, rate, interest):
    answer = round(float(interest / ((rate / 100) * principal / 12)), 2)
    guess = float(input('How long was ${0:,.2f} invested for if the the rate was {1:.2f}% and ${2:,.2f} was earned. '.format(principal, rate, interest)))
    if guess == float(answer):
        correctResult(answer, '', '', ' months.')
    else:
        wrongResult(answer, '', '', ' months.')

def findSimRate(principal, interest, time):
    answer = round(float(interest / (principal * (time / 12)) * 100), 2)
    guess = float(input('What is the rate if ${0:,.2f} was invested for {1:.2f} months and ${2:,.2f} was earned. '.format(principal, time, interest)))
    if guess == float(answer):
        correctResult(answer, '', '', '%.')
    else:
        wrongResult(answer, '', '', '%.')

options = {'Simple Interest': '1.', 'Compound Interest': '2.',
           'Ordinary Simple Annuities': '3.'}

simpleIntOptions = {'Find the Interest': '1.', 'Find the Principal': '2.',
                    'Find the Time': '3.', 'Find the Rate':'4.',
                    'Return to Main Menu': '5.'}

while mainMenuChoice != 999:
    menu(options, 25, 25)
    mainMenuChoice = int(input('\nWhat topic would you like to cover? Press \'999\' to quit.'))

    if mainMenuChoice == 1:             #Simple Interest Quiz Options
        simpleInterestMenu(simpleIntOptions, 25, 25)
        subMenuChoice = int(input('\nWhat type of question do you want to practice with? '))

        if subMenuChoice == 1:         #Find the Simple Interest
            while subMenuChoice == 1:
                findSimInterest(simPrin(), simRate(), simTime())

        elif subMenuChoice == 2:        #Find the Principal
            while subMenuChoice == 2:
                findSimPrincipal(simRate(), simTime(), simInterest())

        elif subMenuChoice == 3:         #Find the Time
            while subMenuChoice == 3:
                findSimTime(simPrin(), simRate(), simInterest())

        elif subMenuChoice == 4:        #Find the Rate
            while subMenuChoice == 4:
                findSimRate(simPrin(), simInterest(), simTime())

        elif subMenuChoice == 5:        #Return to Main Menu
            continue

        else:
            print('Not a valid option. Returning to main menu.')
            time.sleep(1)

    elif mainMenuChoice == 2:
        pass
    elif mainMenuChoice == 999:
        break
    else:
        print('Not a valid option. Try again or select \'999\' to exit.')