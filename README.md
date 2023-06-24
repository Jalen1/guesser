# Guessing Game
## By Jalen Wu

A reinterpretation of the classic "Guess the Number" game in which players must guess a randomly generated number in a given range. 
My version of the game implements a player vs computer feature, in which the player can either:
1. Win, if they correctly guess the number before the computer can.
2. Lose, if the computer guesses the number before the player does.
3. Tie, if the computer and the player get the number with the same amount of guesses.

The bot that the player plays against uses a Binary Search Tree algorithm designed in python:

1. The bot starts their search at the median of the range of guessable integers. The median will be their guess for the number.
2. If the bot detects that the answer is higher than their initial guess, it will narrow its search to the top half of the range and check the median of the new range.
3. Conversely, the bot will do the same but in the lower half if it detects that the answer is lower than their initial guess.
4. The bot will repeat until the algorithm leads them to the exact integer answer.

A list is used to store all of the indices that the bot searches, both to show the player that the bot is legitimate and to showcase the logic behind the 
Binary Search Tree algorithm. 

Text emoji are also implemented in the game to add life to the simple mechanics of the game. (づ ◕‿◕ )づ
