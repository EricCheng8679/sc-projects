"""
File: boggle.py
Name: Eric Cheng
----------------------------------------
TODO:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'

# Global variable
vocab_dic = {}


def main():
    """
    This program is boggle game with a 4x4 board. The input is limited to the form of four letters separated by space,
    i.e "a b c d" which is case-insensitive. Each grid is represented by (j,i) where j is coordinate of y axis and i
    is coordinate of x axis.
    """
    # start = time.time()
    ####################
    matrix_dic = {}
    for y in range(4):
        while True:
            row = input(f'{y + 1} row of letters: ')
            if len(row) == 7 and len(row.split()) == 4:
                matrix_dic[y] = row.split()
                for x in range(4):
                    matrix_dic[y][x] = matrix_dic[y][x].lower()
                break
            else:
                print('Illegal input')
    start = time.time()
    read_dictionary()
    find_boggle(matrix_dic)
    end = time.time()
    ####################
    # end = time.time()
    print('----------------------------------')
    print(f'The speed of your boggle algorithm: {end - start} seconds.')


def find_neighbors(start_coordinate, matrix):
    """
    The function finds all neighbors of start_coordinate,but not includes itself.
    :param start_coordinate: [y,x]
    :param matrix: 4x4 alphabet
    :return: neighbor_position_lst: a list of letters and coordinates of neighbors [[letter1,[y1,x1]],[letter2,[y2,x2]],....]
    """
    neighbor_position_lst = []
    x = start_coordinate[1]
    y = start_coordinate[0]
    for i in range(-1, 2):  # getting neighbors' coordinates by using -1,0,1 to permute
        for j in range(-1, 2):
            letter_x = x + i
            letter_y = y + j
            if 0 <= letter_x <= len(matrix[y]) - 1:
                if 0 <= letter_y <= len(matrix) - 1:
                    if letter_x != x or letter_y != y:
                        letter_and_absolute_position_index = [matrix[letter_y][letter_x], [y + j, x + i]]
                        neighbor_position_lst.append(letter_and_absolute_position_index)
    return neighbor_position_lst


def find_boggle(matrix):
    """
    Select the first letter from left to right and top to bottom.
    """
    word_lst = []                                            # Storing words found
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            cur_string = matrix[y][x]                        # The first letter
            start_coordinate = [y, x]
            existing_ele_position_lst = [start_coordinate]   # Recording the coordinates of grids that have been used
            neighbor_lst = find_neighbors(start_coordinate, matrix)
            helper(start_coordinate, matrix, neighbor_lst, cur_string, word_lst, existing_ele_position_lst)
    print(f'There are {len(word_lst)} words in total.')


def helper(cur_coordinate, matrix, neighbor_lst, cur_string, word_lst, existing_ele_position_lst):
    """
    :param cur_coordinate:  Record the coordinate of the last letter in cur_string
    :param matrix: 4x4 alphabet
    :param neighbor_lst: Record letters and coordinates of neighbors of the last letter in cur_string
    :param cur_string: current string
    :param word_lst: Record words found
    :param existing_ele_position_lst: Record the coordinates of the letter in current string
    """
    if len(neighbor_lst) == 0:
        if cur_string in vocab_dic[cur_string] and len(cur_string) >= 4 and cur_string not in word_lst:
            word_lst.append(cur_string)
            print(f'Found "{word_lst[-1]}"')

    else:
        if neighbor_lst[-1][1] in existing_ele_position_lst:  # Every letter grid can only be passed through once
            neighbor_lst.pop()
            helper(cur_coordinate, matrix, neighbor_lst, cur_string, word_lst, existing_ele_position_lst)
        else:
            # Choose (from the end)
            ele_sub_lst = neighbor_lst.pop()
            ele = ele_sub_lst[0]
            cur_coordinate = ele_sub_lst[1]
            cur_string += ele
            existing_ele_position_lst.append(cur_coordinate)
            # Explore
            if has_prefix(cur_string):
                next_neighbor_lst = find_neighbors(cur_coordinate, matrix)
                helper(cur_coordinate, matrix, next_neighbor_lst, cur_string, word_lst, existing_ele_position_lst)
            # Un-choose
            existing_ele_position_lst.pop()
            cur_string = cur_string[:-1]
            cur_coordinate = existing_ele_position_lst[-1]
            helper(cur_coordinate, matrix, neighbor_lst, cur_string, word_lst, existing_ele_position_lst) # To find other neighbors


def read_dictionary():
    """
    To load the dictionary by all existing prefixes separately.
    """
    with open(FILE, 'r') as f:
        for line in f:
            word = line.strip()
            for i in range(len(word)):
                if word[0:i + 1] not in vocab_dic:
                    vocab_dic[word[0:i + 1]] = [word]
                else:
                    vocab_dic[word[0:i + 1]].append(word)


def has_prefix(sub_s):
    """
    :param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
    :return: (bool) If there is any words with prefix stored in sub_s
    """
    if sub_s in vocab_dic:
        return True
    else:
        return False


if __name__ == '__main__':
    main()
