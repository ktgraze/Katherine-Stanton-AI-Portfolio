# Name: Katherine Stanton
# Date: 12-3-24
# Program: Magic 8-Ball
# Description: This program creates a simple Magic 8-Ball game, which prompts the user to ask a yes/no question, after which\
# the program will randomly choose 1 of 8 possible responses. Next the program asks the user if they want to ask another question.\
# If yes, the game loops and continues. If no, the game ends with a farewell message. 

# import the random module to later call the random.randint() function.
import random

# CONSTANTS
# Assigns constant variables to a welcome and farewell message, a decorative banner, and creates a list of strings\
# of 8 possible responses the Magic 8-Ball will respond with.

WELCOME = "Welcome to the Magic 8-Ball!"
FAREWELL = "Thank you for playing the Magic 8-Ball!"
BANNER = ("~🎱~" * 10)

MAGIC_8_BALL_RESPONSES = [
    "Girl, you know it.",
    "Without a single doubt.",
    "Naur.",
    "Ask me again after I've had coffee.",
    "I fear so.",
    "Tragically, yes.",
    "Fortunately, no.",
    "STOP. Hammer-time!"
]

# Function prints the WELCOME message, prompts the user for a yes/no question and assigns the variable "question" to the user input.\
# Then displays the banner.
def get_user_question():
    print(WELCOME)
    question = input("Ask your yes or no question: ")
    print(BANNER)
    return question

# Function generates a random response from the Magic 8-Ball response list by first generating a random interger using the \
# random.randit(), the random integer generated is then indexed into the response list and corresponds to a random response.
def generate_random_response():
    random_number = random.randint(0, 7)
    return MAGIC_8_BALL_RESPONSES[random_number]

# Function initiates a single round of the game, first by calling the user's input, printing the input, then calling the function\
# to generate a random response from the list and then displays the random response to the user.
def play_game():
    question = get_user_question()
    print("\nYou asked:", question)
    
    response = generate_random_response()
    print("\nMagic 8-Ball says:", response)

# The main() function controls the overall game, repeatedly looping until the user answers "no" to asking another question.\
# First the function calls the play_game() function which initiates one round of the game. Next, the nested "while True" statement\
# asks the user if they want to ask another question and assigns the input to the "play_again" variable. The if/elif/else statement\
# accounts for all possible user inputs: if the user responds "yes" the game iterates again. If else the user responds "no"\
# the game terminates, first printing the FAREWELL message and then the BANNER. The else statement accounts for if a user enters\
# an input other than "yes/ no" and will prompt the user again to respond with either yes or no. 
def main():
    while True:
        play_game()
        
        while True:
            play_again = input("\nDo you want to ask another question? (yes/no): ").lower()
            if play_again == "yes":
                break
            elif play_again == "no":
                print(FAREWELL)
                print(BANNER)
                return
            else:
                print("Please answer with 'yes' or 'no'.")

# Checks if the script is being run directly by Python and if so, calls the main function which initiates the game. 
if __name__ == "__main__":
    main()
