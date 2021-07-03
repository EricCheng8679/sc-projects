"""
File: hailstone.py
Name:Eric Cheng
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    This program executes Hailstone sequences.If the number of input is odd (except for 1),it would be
    multiplied 3 and plus 1.On the other hand,if it is even ,it would be divided by 2.
    Above steps would be repeated until number of output is 1.At the end,this program will show how
    many steps the number of input needs to reach 1.
    """
    print('This program computes Hailstone sequences.')
    a = int(input('Enter a number: '))
    n = 0
    while a != 1:
        if a % 2 == 1:                                                      # a is odd
            b = 3 * a + 1
            print(str(int(a)) + ' is odd, so I make 3n+1: ' + str(int(b)))  # int() ensures no floating point
            a = b                                                           # is displayed (25)
            n += 1                                                          # Re-assign value of a (26)
        else:                                                               # a is even
            b = a / 2
            print(str(int(a)) + ' is even, so I take half: ' + str(int(b)))
            a = b
            n += 1
    print('It took ' + str(n) + ' steps to reach 1.')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
    main()
