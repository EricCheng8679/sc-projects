"""
File: caesar.py
Name: Eric Cheng
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    The secret number determines how many times ALPHABET should be shifted to the right.
    Next, we find the index of the ciphered string in the shifted ALPHABET,and then
    correspond to the original ALPHABET to decipher encrypted string.
    """
    right_shift_n = int(input('Secret Number: '))
    ciphered_string = input("What's the ciphered string?")
    ciphered_string = ciphered_string.upper()
    new_alphabet = right_shift(ALPHABET, right_shift_n)
    deciphered_string = decryption(new_alphabet, ALPHABET, ciphered_string)
    print('The ciphered string is: ' + str(deciphered_string))


def right_shift(string, n):
    """
    :param string: ALPHABET
    :param n: how many times string would be shifted
    :return: a shifted string by n
    """
    new_string = ''
    k = 0
    for i in range(n):              # concatenating the letters that move from the end to the front firstly
        ch = string[len(string) - n + k]
        if len(string) - n + k <= len(string):
            new_string += ch
            k += 1
    for i in range(len(string)-n):  # concatenating the letters which are at the beginning of original string
        ch = string[i]
        new_string += ch
    return new_string


def decryption(shifted_string, string, ciphered_string):
    """
    :param shifted_string: shifted ALPHABET
    :param string: ALPHABET
    :param ciphered_string: the ciphered content we typed in
    :return: deciphered content
    """
    deciphered_string = ''
    for ch in ciphered_string:
        if ch in shifted_string:
            i = shifted_string.find(ch)  # finding the index used for matching the letter in ALPHABET
            deciphered_string += string[i]
        elif ch == ' ':                  # the character we cannot find in ALPHABET
            deciphered_string += ' '
        elif ch == '!':                  # the character we cannot find in ALPHABET
            deciphered_string += '!'

    return deciphered_string


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
