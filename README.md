# numberguess
The user is prompted to input the upper and lower bounds for the range of numbers they want to guess between.

A random number y is generated within the specified range using random.randint(lower, upper).

The program initializes a counter variable count to keep track of the number of guesses.

The game is played in a while loop that continues until one of the following conditions is met:

The user correctly guesses the random number.
The user exceeds the maximum number of allowed guesses, which is determined by math.log(upper - lower + 1, 2).
Inside the loop, the user is prompted to enter their guess x.

The program checks whether x is equal to y. If they match, it prints a congratulatory message and the number of tries it took to guess correctly.

If x is not equal to y, the program provides feedback to the user. If x is greater than y, it informs the user that they guessed too high. If x is less than y, it informs the user that they guessed too low.

The loop continues until the user guesses correctly or until they exceed the maximum allowed guesses.

If the loop exits because the user used all their allowed guesses, the program reveals the correct number y.

Overall, this is a simple number guessing game where the user tries to guess a random number within a specified range. The program provides feedback to help the user narrow down their guess, and it keeps track of the number of attempts. If the user doesn't guess correctly within the allowed number of attempts, the correct number is revealed.
# wordguess
The player is asked to enter their name, and a welcome message is displayed.

There's a predefined list of words from which the computer selects one randomly.

The program initializes an empty string called guesses to store the characters guessed by the player.

The player is given a fixed number of turns (12 in this case) to guess the word.

Inside the while loop, the program checks if the player has guessed all the characters in the word:

It initializes a variable called failed to 0.
It then iterates through each character in the word. If the character is in the guesses string, it's displayed; otherwise, an underscore (_) is displayed to represent an unguessed character, and the failed count is incremented.
If failed remains 0 after looping through the characters, it means the player has guessed all the characters in the word, and a "You Win" message is displayed along with the correct word.

If the player hasn't guessed all the characters in the word, the program continues to the next turn:

The player is prompted to guess a character.
The guessed character is added to the guesses string.
If the guessed character is not in the word, the turns counter is decreased, and a "Wrong" message is displayed along with the number of remaining guesses.
The loop continues until the player either guesses the word correctly (winning) or runs out of turns (losing).

If the player runs out of turns, a "You Lose" message is displayed.

Overall, this code provides a simple word guessing game where the player tries to guess a word, and they have a limited number of attempts to do so. If they guess all the characters in the word correctly within the allotted number of turns, they win. Otherwise, they lose.
