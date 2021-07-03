"""
File: complement.py
Name: Eric Cheng
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    The program provides the function to find out complement strand by typing a sequence of DNA.
    The complementary pairs are 'A to T','T to A','C to G' and 'G to C'. In addition, this program is case-
    insensitive,thus the input can be the combination of 'a','A','t','T','c','C','g','G'.
    """
    while True:
        dna = input("Please give me a DNA strand and I'll find the complement: ")
        dna = dna.upper()
        if 'B' not in dna and 'D' not in dna and 'E' not in dna and 'F' not in dna and 'H' not in dna and 'I' not \
            in dna and 'J' not in dna and 'K' not in dna and 'L' not in dna and 'M' not in dna and 'N' not in dna \
            and 'O' not in dna and 'P' not in dna and 'Q' not in dna and 'R' not in dna and 'S' not in dna and 'U' \
                not in dna and 'V' not in dna and 'W' not in dna and 'X' not in dna and 'Y' not in dna and 'Z':
            break  # a DNA strand doesn't contain letters other than A,T,C,G
    com_dna = build_complement(dna)
    print('The complement of ' + str(dna) + ' is ' + str(com_dna))


def build_complement(dna):
    """
    :param dna: dna string
    :return ans : the complement strand of dna
    """
    ans = ''
    for base in dna:
        if base == 'A':
            ans += 'T'
        elif base == 'T':
            ans += 'A'
        elif base == 'C':
            ans += 'G'
        elif base == 'G':
            ans += 'C'
    return ans


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
