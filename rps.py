import random

print("\n")

user_name_input = input("What is your name?: ")
print(f"Oh hello {user_name_input}!")
print("\n")

instructions = """
WELCOME TO ROCK, PAPER, SCISSORS!

IT'S THE CLASSIC GAME YOU KNOW!

ROCK DESTROYS SCISSORS
PAPER COVERS ROCK
SCISSORS CUTS PAPER

TYPE IN YOUR CHOICE WHEN ASKED TO SHOOT!

THE FIRST TO REACH 3 POINTS, WINS!

WE WISH YOU ALL THE BEST!
"""
print(instructions)


while True:
    user_playing = input(
        "Do you want to play? (Type in a yes or no): ").lower()
    if user_playing == "yes":
        print("Okay great! But first...")
        print("\n")
    elif user_playing == "no":
        print("Ok...sad")
        quit()
    else:
        print("Please type in a valid response")
        continue

    # nested while True block gets user's age and ensures that:
    # they are old enough
    # they typed in the correct age

    while True:
        try:
            user_age_input = int(input("How old are you?: "))
            if user_age_input >= 8:
                print("Ok you are old enough, welcome aboard!")
                print("\n")

            else:
                print("Sorry you are too young to play!")
                quit()

        except ValueError:
            print("Invalid input, please type in a (whole) number")
            continue

    # user and computer choice

        options = ["rock", "paper", "scissors"]

        user_points = 0
        comp_points = 0

        while True:
            print("ROCK--PAPER--SCISSORS!")
            user_choice = input("SHOOT!: ").lower()
            comp_choice = random.choice(options)

            if user_choice not in options:
                print("Please choose either rock, paper or scissors")
                print("\n")
                continue

            # CONDITIONS
            if user_choice == "rock" and comp_choice == "scissors":
                print("WIN")
                print(f"Computer's Choice: {comp_choice}")
                user_points += 1
                print(f"Your Points: {user_points}")
                print(f"Computer's Points: {comp_points}")

                print("\n")

            elif user_choice == "paper" and comp_choice == "rock":
                print("WIN")
                print(f"Computer's Choice: {comp_choice}")
                user_points += 1
                print(f"Your Points: {user_points}")
                print(f"Computer's Points: {comp_points}")

                print("\n")
            elif user_choice == "scissors" and comp_choice == "paper":
                print("WIN")
                print(f"Computer's Choice: {comp_choice}")
                user_points += 1
                print(f"Your Points: {user_points}")
                print(f"Computer's Points: {comp_points}")

                print("\n")

            elif user_choice == comp_choice:
                print(f"Computer's Choice: {comp_choice}")
                print("Same picks, play again")
                print(f"Your Points: {user_points}")
                print(f"Computer's Points: {comp_points}")
                print("\n")
            else:
                print("LOSS")
                print(f"Computer's Choice: {comp_choice}")
                comp_points += 1
                print(f"Your Points: {user_points}")
                print(f"Computer's Points: {comp_points}")
                print("\n")

            if user_points == 3:
                print("You've won")
                print(
                    f"You did it {user_name_input}!, you're a rock, paper, scissors MASTER!!!!")
                quit()

            elif comp_points == 3:
                print("You've lost")
                print(f"Sorry {user_name_input}, you'll get it next time!")
                quit()

    #       play_again = input("Do you want to play again?: ").lower()

    #     if play_again == "yes":
    #         print("Great! Let's go!")
    #         print("\n")
    #         continue
    #     else:
    #         play_again == "no"
    #         print("Ok thanks for playing")
    #         quit()
    # break
