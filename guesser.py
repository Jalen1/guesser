# Guessing Game
# By: Jalen Wu
# Objective: Implement a Binary Search Tree the user must compete against to find a randomly generated number.

import random

# To run the game.
def guessing_game():
    for i in range(5):
        print("")
    print("(ᵔᴥᵔ):   Hello User! Welcome to the Guessing Game.")
    print("")
    print("(｡◕‿◕｡): To win, you must correctly guess a randomly generated number in a range of numbers you provide.")
    print("")

    min = int(input("༼ つ ◕_◕ ༽つ: First, please enter the minimum integer value of your number: "))
    print("")
    max = int(input("(~˘▾˘)~:   Now, please enter the maximum integer value of your number: "))
    print("")

    # In the case that user tries to enter a lower maximum value.
    if max <= min:
        raise Exception("maximum value must be higher than minimum. Closing program.")

    target = random.randrange(min, max)
    is_game_over = False
    guess_count = 0

    # For testing purposes
    # print("The answer is:", target)

    # Controls the game and continuously iterates until the user correctly guesses the number.
    while (is_game_over != True):
        
        # To invoke the robot guesser and store its guesses as a python list.
        robot_list = bot_bst(min,max,target)

        # Asks the player to enter guesses and analyzes input to give feedback to the user.
        guess = int(input("ᕙ(⇀‸↼‶)ᕗ :    Please enter your guess: "))
        print("")

        if (guess > target):
            print("⚆ _ ⚆ :     Too high!")
            print("")
            guess_count = guess_count + 1
        elif (guess < target):
            print("¬_¬:     Too low!")
            print("")
            guess_count = guess_count + 1
        else:
            guess_count = guess_count + 1
            if(guess_count < len(robot_list)):       
             print("")
             print("(ﾉ◕ヮ◕)ﾉ*:  YOU WIN!!!    *ヽ(◕ヮ◕ヽ)")
             print("")
             print("You correctly guessed the number in", guess_count,"guesses.")
             print("You beat our robot, who got the number in", len(robot_list), "guesses")
             print("The numbers they guessed were:", robot_list)
             print("")
             print("(ﾉ◕ヮ◕)ﾉ*:  YOU'RE SO COOL!!!    *ヽ(◕ヮ◕ヽ)")
             print("")
            elif(guess_count == len(robot_list)):
             print("")
             print("ヾ(⌐■_■)ノ♪:   TIE!!!")
             print("")
             print("You correctly guessed the number in", guess_count,"guesses.")
             print("You tied with our robot, who ALSO got the number in", len(robot_list), "guesses")
             print("The numbers they guessed were:", robot_list)
             print("")
             print("(ᵔᴥᵔ):  Better luck next time!")
             print("")
            else:
             print("")
             print("╥﹏╥     YOU LOSE!!!     ╥﹏╥")
             print("")
             print("You correctly guessed the number in", guess_count,"guesses.")
             print("You lost to our robot, who got the number in", len(robot_list), "guesses")
             print("The numbers they guessed were:", robot_list)
             print("")
             print("(ᵔᴥᵔ):  Better luck next time!")
             print("")
            is_game_over = True
            break

# To implement a Binary Search Tree algorithm to play against the player.
def bot_bst(minimum, maximum, target_num) -> list():
    bot_guess = int((minimum + maximum) / 2)
    thislist = [bot_guess]
    while(bot_guess != target_num):
        if bot_guess > target_num:
            maximum = bot_guess
            bot_guess = int((minimum + maximum) / 2)
            thislist.append(bot_guess)
        elif bot_guess < target_num:
            minimum = bot_guess
            bot_guess = int((minimum + maximum) / 2)
            thislist.append(bot_guess)

    return thislist


guessing_game()