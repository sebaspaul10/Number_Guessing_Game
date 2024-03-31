import random  # Importing the random module to generate random numbers

print("Welcome to your number guessing game !!!")  # Displaying a welcome message to the user

# Providing instructions for the game
print("To win you need to guess the same number as the computer")
print("Enter the interval that you want to guess the number")

# Define a function to get the number of lives from the user
def life_user():
    while True:
        try:
            life = int(input("How much life you want ? : "))  # Prompting the user to input the number of lives
            return life  # Returning the number of lives entered by the user
        except ValueError:
            print("Error, please enter a number !!!")  # Handling non-integer inputs
            continue

# Define a function to get the starting number of the interval from the user
def first_interval():
    while True:
        try:
            num1 = int(input("From : "))  # Prompting the user to input the starting number of the interval
            return num1  # Returning the starting number of the interval entered by the user
        except ValueError:
            print("Error, please enter a number !!!")  # Handling non-integer inputs
            continue

# Define a function to get the ending number of the interval from the user
def last_interval():
    while True:
        try:
            num2 = int(input("To : "))  # Prompting the user to input the ending number of the interval
            return num2  # Returning the ending number of the interval entered by the user
        except ValueError:
            print("Error, please enter a number !!!")  # Handling non-integer inputs
            continue

# Define the main guessing game function
def guessing_game(life, num1, num2):
    your_num = 0
    computer_num = 0

    # Loop for the number of lives
    for i in range(life):
        computer_guess = random.randint(num1, num2)  # Generating a random number for the computer's guess
        print(computer_guess)  # Printing the computer's guess (for debugging)

        # Loop for user's guess input
        while True:
            try:
                your_guess = int(input(f"Enter guess {i + 1} : "))  # Prompting the user to input their guess
                break  # Exiting the loop if the input is valid
            except ValueError:
                print("Error, Please enter a number !!!")  # Handling non-integer inputs
                print()
                continue

        # Checking if the user's guess matches the computer's guess
        if your_guess == computer_guess:
            print(f"The computer guess {computer_guess}")
            print("You guessed the same number as the computer !!!")
            print()
            your_num += 1  # Incrementing user's score if they guessed correctly

        else:
            print(f"The computer guess {computer_guess}")
            print("You didn't guess the same number as the computer !!!")
            print()
            computer_num += 1  # Incrementing computer's score if user's guess is incorrect

    # Determining the outcome of the game
    if your_num > computer_num:
        print(f"You won {your_num} - {computer_num}!!!")
        print()
    elif computer_num > your_num:
        print(f"You lost {computer_num} - {your_num} against the computer !!!")
        print()
    else:
        print(f"It's a tie {computer_num} - {your_num}")
        print()

# Getting user inputs for game setup
life1 = life_user()
num1 = first_interval()
num2 = last_interval()

# Running the guessing game with user inputs
guessing_game(life1, num1, num2)

# Asking the user if they want to play again
while True:
    question = input("Want to try again, yes or no ? : ")
    if question.lower() == "yes":
        num1 = first_interval()
        num2 = last_interval()
        life1 = life_user()
        guessing_game(life1, num1, num2)
    elif question.lower() == "no":
        print("Goodbye !!!")
        break
    else:
        print("Error !!!")
        continue
