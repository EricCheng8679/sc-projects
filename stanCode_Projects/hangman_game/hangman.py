"""
File: hangman.py
Name: Eric Cheng
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    We have to confirm the edge case before the game starts.Whenever we type in correct letter,
    it will be recorded. Therefore, no matter whether the next letter is correct or not,all known
    letters will be displayed. In addition, the input is limited to alphabet, case-sensitive and
    only one letter at a time.
    """
    length_word = ''
    word = random_word()
    life = N_TURNS
    for i in range(len(word)):                 # edge case
        length_word += '-'
    print('The word looks like: ' + str(length_word))
    print('You have ' + str(life) + ' guesses left.')
    known_letter = ''                          # for recording the words we guessed right
    known_word = length_word
    while True:
        guess = input('Your guess: ')
        guess = guess.upper()
        known_word = known_word                # recording current known word for displaying in case of guessing wrong
        if not guess.isalpha() or len(guess) > 1:
            print('illegal format.')
        elif guess in word:
            known_word = ''                    # for concatenating known word
            for k in range(len(word)):
                if guess == word[k]:           # concatenating the letter we guessed right based on its position in word
                    known_word += guess
                elif word[k] in known_letter:  # concatenating known letters based on their positions in word
                    known_word += word[k]
                else:                          # concatenating unknown word with -
                    known_word += '-'
            known_letter += guess
            print('You are correct!')
            if '-' not in known_word:          # guessing right all letters, jumping out of loop
                print('You win!!')
                print('The word was: ' + str(known_word))
                break
            else:
                print('The word looks like: ' + str(known_word))
                print('You have ' + str(life) + ' guesses left.')
        else:                                  # guessing wrong
            life -= 1                          # less one life whenever we guess wrong letter
            print("There is no " + str(guess) + "'s in the word.")
            if life == 0:                      # game fail, jumping out of loop
                print('You are completely hung : (')
                print('The word was: ' + str(word))
                break
            else:
                print('The word looks like: ' + str(known_word))
                print('You have ' + str(life) + ' guesses left.')


def random_word():
    """
    This function is a table of random words
    :return: string : a word for guessing
    """
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
