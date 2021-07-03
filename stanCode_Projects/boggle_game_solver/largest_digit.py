"""
File: largest_digit.py
Name: Eric Cheng
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
    print(find_largest_digit(12345))      	# 5
    print(find_largest_digit(281))        	# 8
    print(find_largest_digit(6))          	# 6
    print(find_largest_digit(-111))         # 1
    print(find_largest_digit(-9453))        # 9


def find_largest_digit(n):
    """
    :param n: an integer
    :return: int : a maximum number among digits
    """
    if n < 0:                                      # Covert to a positive integer
        n = -n
    power = 0                                      # The power of 10
    max_num = n % 10                               # Initial case
    return helper(n, max_num, power)


def helper(n, max_num, power):
    if max_num * (10 ** power) >= n:               # Base case
        return max_num
    else:
        power += 1
        if int(n / (10 ** power) % 10) > max_num:  # Taking the number of digits to compare with previous one
            max_num = int(n / (10 ** power) % 10)
        return helper(n, max_num, power)           # To share all variables of a function among stack frame


if __name__ == '__main__':
    main()
