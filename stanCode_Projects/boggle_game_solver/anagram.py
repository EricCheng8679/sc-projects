"""
File: anagram.py
Name: Eric Cheng
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time  # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'  # This is the filename of an English dictionary
EXIT = '-1'  # Controls when to stop the loop

vocab_dic = {}


def main():
    """
    The program finds anagrams of word we type in by using recursion and dictionary of data structure.
    """
    # To test how fast all anagrams are found
    ####################
    print(f"Welcome to stanCode \"Anagram Generator\" (or -1 to  quit)")
    word = input("Find anagrams for: ")
    read_dictionary()
    start = time.time()
    find_anagrams(word)
    end = time.time()
    ####################

    # start = time.time()
    # ####################
    # print(f"Welcome to stanCode \"Anagram Generator\" (or -1 to  quit)")
    # read_dictionary()
    # while True:
    #     word = input("Find anagrams for: ").lower()  # case-insensitive
    #     if word == EXIT:
    #         break
    #     find_anagrams(word)
    # ####################
    # end = time.time()
    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end - start} seconds.')


def read_dictionary():
    """
    To separate the dictionary by all existing prefixes.
    """
    with open(FILE, 'r') as f:
        for line in f:
            word = line.strip()
            for i in range(len(word)):  #把每個可能出現字母都找進去
                if word[:i + 1] not in vocab_dic:
                    vocab_dic[word[:i + 1]] = [word]
                else:
                    vocab_dic[word[:i + 1]].append(word)


def find_anagrams(s):
    """
    :param s: word we type in
    :return:
    """
    s_len = len(s)
    anagrams_list = []  # To store the permutation existing in dictionary
    anagram = ''  # To store the permutation of word
    anagram_index_list = []  # To put the permutation of word's indexes
    print('Searching')
    helper(s, s_len, anagram, anagrams_list, anagram_index_list)
    print(f'{len(anagrams_list)} anagrams: {anagrams_list}')


def helper(s, s_len, anagram, anagrams_list, anagram_index_list):
    """
    The function finds the permutation of letter in word we typed in and then check whether it is in the dictionary.
    The permutation way is using the index of the letters to arrange to avoid the situation where repeated
    letters cannot be arranged.
    :param s: word we typed in
    :param s_len: length of word
    :param anagram: the permutation of letter in word
    :param anagrams_list: a list storing anagrams
    :param anagram_index_list: the permutation of letter's index in word
    """
    if len(anagram) == s_len:  # Base case
        if anagram in vocab_dic[anagram] and anagram not in anagrams_list:  # To avoid putting repeated anagram into anagrams_list
            print(f'Found:  {anagram}')
            anagrams_list.append(anagram)
            print('Searching...')
    else:
        for i in range(s_len):
            if i in anagram_index_list:
                pass
            else:  #可用.remove做
                anagram += s[i]  # choose
                anagram_index_list.append(i)
                if has_prefix(anagram):
                    helper(s, s_len, anagram, anagrams_list, anagram_index_list)  # explore
                anagram_index_list.pop()  # un-choose
                anagram = anagram[:-1]


def has_prefix(sub_s):
    """
    :param sub_s:
    :return:
    """
    if sub_s in vocab_dic:
        return True
    else:
        return False

    # The code before optimization (just for memorialization)
    # dic = vocab_dic[sub_s[0]]
    # for i in range(len(sub_s)):
    #     if sub_s[0:-i] in vocab_dic:
    #         dic = vocab_dic[sub_s[:-i]]
    #         break
    #
    # has_prefix_or_not = False
    # for word in dic:
    #     if word.startswith(sub_s):
    #         has_prefix_or_not = True
    #         break
    # return has_prefix_or_not


if __name__ == '__main__':
    main()

