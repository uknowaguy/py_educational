#Educational Games
#Steven William

def continue_or_quit():
    choice = input("Enter (y) for yes and continue to play\n"
                   "Enter (n) for no and exit game\n").lower()
    if choice == "n".lower():
        for x in range(0,20):
            print("\n")
        main()

#english game

def mad_Lib_Boy(noun1, adjective1, verb1):
    print(
        f"There was once a {adjective1} boy named, "
        f"{noun1}, he loved to do all sorts of things. "
        f"Even though this was true his favorite thing "
        f"to do was to {verb1}\n")


def mad_Lib_Girl(noun1, adjective1, verb1):
    print(f"A girl that was {adjective1}, loved to {verb1} all day long and she loved doing at her favorite {noun1}.\n")


def mad_Lib():
    choice = "continue"

    while choice != "quit" or "q":
        print("It is time to learn how to use nouns, adjectives, and verbs!")

        noun1 = input("Enter a noun, remember a noun is a person or place.\n\n").upper()
        adjective1 = input("Enter an adjective, remember an adjective is a description of something.\n\n").upper()
        verb1 = input("Enter a verb, remember a verb is an action, someone is doing something.\n\n").upper()

        mad_Lib_Boy(noun1, adjective1, verb1)
        mad_Lib_Girl(noun1, adjective1, verb1)

        print("Do you want to keep learning through the fun world of Mad Libs!\n")

        continue_or_quit()

    print("Thank you for playing with us!\n")

# Math Game

def math_game():
    import random

    print("Lettuce Play A Game of Math\n"
          "Do you wanna play?\n")

    choice = input("Enter (y) for yes and continue to play\n"
                   "Enter (n) for no and exit game\n").lower()
    if choice == "n".lower():
        main()

    while choice == "y":
        # first_number = 0
        first_number = random.randrange(0, 10)
        second_number = random.randrange(0, 10)

        operator = input("Press A for addition \n"
                         "Press S for subtraction \n"
                         "Press M for Multiplication \n"
                         "Press D for division \n")
        if operator == "a" or operator == "A":
            result = first_number + second_number
            users_answer = input(f"{first_number} + {second_number} = ")
            users_answer = int(users_answer)
            print(f"You entered {users_answer}")
            if users_answer == result:
                print(f"{first_number} + {second_number} = {result}")
            elif users_answer > result:
                print(f"You almost had it\nYou are off by {users_answer - result} \nCorrect answer is {result}")
            elif result > users_answer:
                print(f"You almost had it\nYou are off by {result - users_answer} \nCorrect answer is {result}")

            print("Would you like to do some math?\n")

            continue_or_quit()

        elif operator == "s" or operator == "S":
            result = first_number - second_number
            users_answer = input(f"{first_number} - {second_number} = ")
            users_answer = int(users_answer)
            print(f"You entered {users_answer}")
            if users_answer == result:
                print(f"{first_number} - {second_number} = {result}")
            elif users_answer > result:
                print(f"You almost had it\nYou are off by {users_answer - result} \nCorrect answer is {result}")
            elif result > users_answer:
                print(f"You almost had it\nYou are off by {result - users_answer} \nCorrect answer is {result}")

            print("Would you like to do some math?\n")
            continue_or_quit()

        elif operator == "m" or operator == "M":
            result = first_number * second_number
            users_answer = input(f"{first_number} * {second_number} = ")
            users_answer = int(users_answer)
            print(f"You entered {users_answer}")
            if users_answer == result:
                print(f"{first_number} * {second_number} = {result}")
            elif users_answer > result:
                print(f"You almost had it\nYou are off by {users_answer - result} \nCorrect answer is {result}")
            elif result > users_answer:
                print(f"You almost had it\nYou are off by {result - users_answer} \nCorrect answer is {result}")

            print("Would you like to do some math?\n")
            continue_or_quit()

        elif operator == "d" or operator == "D":
            if first_number == 0:
                first_number = first_number + 1
            elif second_number == 0:
                second_number = second_number + 1
            elif second_number == 0 and first_number == 0:
                first_number = first_number + 1
                second_number = second_number + 1
            else:
                result = first_number / second_number
                users_answer = input(f"{first_number} / {second_number} = ")
                users_answer = float(users_answer)
                print(f"You entered {users_answer}")
                if users_answer == result:
                    print(f"{first_number} / {second_number} = {result}")
                elif users_answer > result:
                    print(f"You almost had it\nYou are off by {users_answer - result} \nCorrect answer is {result}")
                elif result > users_answer:
                    print(f"You almost had it\nYou are off by {result - users_answer} \nCorrect answer is {result}")

            print("Would you like to do some math?\n")
            continue_or_quit()

        else:
            print("Would you like to do some math?\n")
            continue_or_quit()

# Points Game (multiple choice)

def questionOne():
    print("First Question for $100\n"
          "Who was the first President of the United States?\n"
          "1. George Washington\n"
          "2. Bob Dole\n"
          "3. John E Kennedy\n"
          "4. Scott Stapp\n")

    answer = input("Enter the number of you choice...\n")

    if answer == "1":
        print(f"You chose {answer}... THAT IS CORRECT!\n")
        money = 100
    else:
        print(f"You chose {answer}... THAT IS WRONG!\n")
        print("NO MONEY FOR YOU!\n")
        money = 0

    return money


def questionTwo():
    print("Second Question for $1000\n"
          "How many sides does a FIVE POINT pentagon have?\n"
          "1. a(4)\n"
          "2. b(3)\n"
          "3. c(2)\n"
          "4. d(5)\n"
          "5. e(7)\n")

    answer = input("Enter the number of you choice...\n")

    if answer == "4":
        print(f"You chose {answer}... THAT IS CORRECT!\n")
        money = 1000
    else:
        print(f"You chose {answer}... THAT IS WRONG!\n")
        print("NO MONEY FOR YOU!\n")
        money = 0

    return money

def questionThree():
    print("Third Question for $10000\n"
          "If you jog 9 miles an hour, how far will you jog in a hour?\n"
          "1. 1\n"
          "2. 19\n"
          "3. 9\n"
          "4. 20\n")

    answer = input("Enter the number of you choice...\n")

    if answer == "3":
        print(f"You chose {answer}... THAT IS CORRECT!\n")
        money = 10000
    else:
        print(f"You chose {answer}... THAT IS WRONG!\n")
        print("NO MONEY FOR YOU!\n")
        money = 0

    return money

def questionFour():
    print("Fourth Question for $100000\n"
          "The majority of spiders have how many eyes?\n"
          "1. 7\n"
          "2. 6\n"
          "3. 8\n"
          "4. 4\n")

    answer = input("Enter the number of you choice...\n")

    if answer == "3":
        print(f"You chose {answer}... THAT IS CORRECT!\n")
        money = 100000
    else:
        print(f"You chose {answer}... THAT IS WRONG!\n")
        print("NO MONEY FOR YOU!\n")
        money = 0

    return money

def questionFive():
    print("Fifth Question for $1000000\n"
          "What do you call the offspring of a male lion and a female tiger?\n"
          "1. Tiglon\n"
          "2. Longer\n"
          "3. Liger\n"
          "4. Litig\n")

    answer = input("Enter the number of you choice...\n")

    if answer == "3":
        print(f"You chose {answer}... THAT IS CORRECT!\n")
        money = 1000000
    else:
        print(f"You chose {answer}... THAT IS WRONG!\n")
        print("NO MONEY FOR YOU!\n")
        money = 0

    return money

def points_game():
    play_again = "y"

    while play_again == "y".lower():
        print("Let's Play. Who Wants To Win Points?\n")
        if play_again == "n".lower():
            main()

        totalMoney = 0

        totalMoney += questionOne()  # will return money and put it in totalMoney
        totalMoney += questionTwo()
        totalMoney += questionThree()
        totalMoney += questionFour()
        totalMoney += questionFive()

        print(f"Congrats! You won ${totalMoney}!\n\n")

        continue_or_quit()

        # print("Do you want to play again? Enter yes or no.\n")
        # playAgain = input()
        # playAgain = playAgain.lower()

    print("Thank you for playing?")

def main():
    choice = input("Enter (e) to play english games\n"
                   "Enter (m) to play math games\n"
                   "Enter (p) to play points game\n")

    if choice == "English" or choice == "e".lower():
        mad_Lib()
    elif choice == "Math" or choice == "m".lower():
        math_game()
    elif choice == "Points" or choice == "p".lower():
        points_game()
    else:
        return main()


if __name__ == "__main__":
    main()