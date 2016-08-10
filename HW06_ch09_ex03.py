#!/usr/bin/env python3
# HW06_ch09_ex03.py

# (1)
# Write a function named avoids that takes a word and a string of forbidden
# letters, and that returns True if the word doesn't use any of the forbidden
# letters.
#   - write avoids
# (2)
# Modify your program to prompt the user to enter a string of forbidden
# letters and then print the number of words that don't contain any of them.
#   - write forbidden_prompt and
#   - modify to create forbidden_param that accepts the string as an argument
# (3)
# Can you find a combination of 5 forbidden letters that excludes the smallest
# number of words?
#   - write a function that finds this combination of letters: find_five
#   - have that function print the letters and print the # of words excluded
##############################################################################
# Imports

# Body


def avoids(word, badword):
    """ return True if word NOT forbidden"""
    for letter in word:
        if badword in letter:
            return False
        else:
            return True


def forbidden_prompt(user_input, user_buzzword):
    """ print count of words NOT forbidden by input"""
    user_buzzword = input("Please type in anything you want to filter:")
    user_input = input("Feel freee to type in anything and I'll let you know: ")
    user_input_list = user_input.split()
    count = 0 
    for words in user_input_list:
        if badword not in words:
            count += 1
    print(count)



def forbidden_param(user_input, badword):
    """ return count of words NOT forbidden by param"""
    user_input = input("Please type in some bad words: ")
    user_input_list = user_input.split()
    count = 0 
    for words in user_input_list:
        if badword in words:
            count += 1
    print(count)


def find_five():
    ...


##############################################################################
def main():
    ...
    # Your final submission should only call five_five

if __name__ == '__main__':
    main()
