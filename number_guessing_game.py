import random # Importing the random module to generate random numbers

print ("Welcome to your number guessing game !!!")

print ("To win you need to guess the same number as the computer")
print ("Enter the interval that you want to guess the number")

def life_user ():
    while True:
        try:
            life = int (input ("How much life you want ? : "))
            return life
        except ValueError:
            print ("Error, please enter a number !!!")
            continue

def first_interval ():
    while True:
        try:
            num1 = int (input ("From : "))
            return num1
        except ValueError:
            print ("Error, please enter a number !!!")
            continue

def last_interval ():
    while True:
        try:
            num2 = int (input ("To : "))
            return num2
        except ValueError:
            print ("Error, please enter a number !!!")
            continue

def guessing_game (life, num1, num2):
    your_num = 0
    computer_num = 0

    for i in range  (life):
        computer_guess = random.randint (num1, num2)
        print (computer_guess) # to check what's the random number

        while True:
            try:
                your_guess = int (input (f"Enter guess{i + 1} : "))
                break
            except ValueError:
                print ("Error, Please enter a number !!!")
                print()
                continue

        if your_guess == computer_guess:
            print (f"The computer guess {computer_guess}")
            print ("You guessed the same number as the computer !!!")
            print()
            your_num = your_num + 1

        if not (your_guess == computer_guess):
            print (f"The computer guess {computer_guess}")
            print ("You didn't guess the same number as the computer !!!")
            print()
            computer_num = computer_num + 1
    if your_num > computer_num:
        print (f"You won {your_num} - {computer_num}!!!")
        print()
    if computer_num > your_num:
        print (f"You lost {computer_num} - {your_num} against the computer !!!")
        print ()
    if computer_num == your_num:
        print (f"It's a tie {computer_num} - {your_num}")
        print ()
    


life1 = life_user()
num1 = first_interval()
num2 = last_interval()
guessing_game (life1, num1, num2)

while True:
    question = input ("Want to try again, yes or no ? : ")
    if question.lower() == "yes":
        num1 = first_interval()
        num2 = last_interval()
        life1 = life_user()
        guessing_game(life1, num1, num2)
    elif question.lower() == "no":
        print ("Goodbye !!!")
        break
    else:
        print ("Error !!!")
        continue