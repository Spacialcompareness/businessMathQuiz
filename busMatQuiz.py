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
    interest = float(random.randint(1, 1000))
    return interest

def findSimInterest():          #Function to find the simple interest
    principal, rate, time = simPrin(), simRate(), simTime()
    answer = round(float(principal * rate / 100 * time / 12), 2)
    guess = float(input('What is the interest earned on ${:,.2f} for '.format(principal) + str(time) +
                        ' months at {:.2f}%?'.format(rate)))
    if guess == float(answer):
        print('You are correct! The answer is {:,.2f}\n'.format(answer))
        simpleInterestMenu(simpleIntOptions, 20, 20)
        subMenuChoice = int(input('\nWhat type of question do you want to practice with? '))
    else:
        print('No, unfortunately the answer is ${:,.2f}\n'.format(answer))
        simpleInterestMenu(simpleIntOptions, 20, 20)
        subMenuChoice = int(input('\nWhat type of question do you want to practice with? '))

def findSimPrincipal():
    rate, time, interest = simRate(), simTime(), simInterest()
    answer = round(float(interest / (rate / 100) * (time / 12)), 2)
    guess = float(input('What is the principal if ${0:,.2f} is earned at {1:.2f}% interest for '.format(interest, rate)
                        + str(time) + ' months.'))
    if guess == float(answer):
        print('You are correct! The answer is {:,.2f}\n'.format(answer))
        simpleInterestMenu(simpleIntOptions, 20, 20)
        subMenuChoice = int(input('\nWhat type of question do you want to practice with? '))
    else:
        print('No, unfortunately the answer is {:,.2f}\n'.format(answer))
        simpleInterestMenu(simpleIntOptions, 20, 20)
        subMenuChoice = int(input('\nWhat type of question do you want to practice with? '))

options = {'Simple Interest': '1.', 'Compound Interest': '2.',
           'Ordinary Simple Annuities': '3.'}

simpleIntOptions = {'Find the Interest': '1.', 'Find the Principal': '2.',
                    'Find the Time': '3.', 'Find the Rate':'4.',
                    'Return to Main Menu': '5.'}

while mainMenuChoice != 999:
    menu(options, 40, 40)
    mainMenuChoice = int(input('\nWhat topic would you like to cover? Press \'999\' to quit.'))

    if mainMenuChoice == 1:             #Simple Interest Quiz Options
        simpleInterestMenu(simpleIntOptions, 20, 20)
        subMenuChoice = int(input('\nWhat type of question do you want to practice with? '))

        if subMenuChoice == 1:         #Find the Simple Interest
            while subMenuChoice == 1:
                findSimInterest()

        elif subMenuChoice == 2:        #Find the Principal
            while subMenuChoice == 2:
                findSimPrincipal()

        elif subMenuChoice == 3:         #Find the Time
            print('3')

        elif subMenuChoice == 4:        #Find the Rate
            print('4')

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
        print('Not a valid option.')