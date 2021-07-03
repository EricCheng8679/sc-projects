"""
File: similarity.py
Name: Eric Cheng
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    The program compares a short DNA sequence with a long sequence and output a subsequence of the long DNA
    sequence which is the most similar to the short DNA sequence.
    The input of DNA sequence is case-insensitive.
    """
    long_dna = input('Please give me a DNA sequence to research: ')
    long_dna = long_dna.upper()
    short_dna = input('What DNA sequence would you like to match: ')
    short_dna = short_dna.upper()
    match_dna = match(long_dna, short_dna)
    print('The best match is: ' + str(match_dna))


def match(long_sequence, short_sequence):
    """
    Finding perfect match based on the length of the short sequence,
    If there is no perfect match, the condition for judging perfect match would be
    subtracted by 1 in order as new condition for judging the most similarity.
    Above steps would be repeated until the best match is found.
    :param long_sequence: long DNA string
    :param short_sequence: short DNA string
    :return:match_dna: the most similar subsequence of long DNA string to short DNA string
    """
    n = 0                                                       # for cutting off the segment of DNA we want to match
    count_same_bases = 0                                        # for counting the number of the same letters
    k = 0                                                       # for lowering the standard for judging similarity
    while len(short_sequence)-k > 0:                            # tackling the situations that don't have perfect match.
        while n != len(long_sequence) - len(short_sequence) + 1:  # all subsequences of adjacent letters in the long se-
            match_dna = long_sequence[n:len(short_sequence)+n]    # quence which equal the length of the short sequence
            for i in range(len(short_sequence)):
                if match_dna[i] == short_sequence[i]:
                    count_same_bases += 1
            if count_same_bases == len(short_sequence)-k:                      # the most similar
                return match_dna
            elif count_same_bases < len(short_sequence)-k:
                n += 1
                count_same_bases = 0
        n = 0
        k += 1


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
