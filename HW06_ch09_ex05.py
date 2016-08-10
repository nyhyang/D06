#!/usr/bin/env python3
# HW06_ch09_ex05.py

# (1)
# Write a function named uses_all that takes a word and a string of required
# letters, and that returns True if the word uses all the required letters at
# least once.
#   - write uses_all
# (2)
# How many words are there that use all the vowels aeiou? How about
# aeiouy?
#   - write functions(s) to assist you
#   - # of words that use all aeiou: [type here]
#   - # of words that use all aeiouy: [type here]
##############################################################################
# Imports

# Body

def uses_all(word, letters):
	count = 0 
	for letter in letters:
		if letter in word:
			count += 1
	if count == len(letters):
		return True
	return False


def uses_all_vowels(lst):
	count = 0 
	vowels = 'aeiou'
	for word in lst:
		if uses_all(word, vowels):
			count += 1
	return count

def uses_all_vowels_y(lst):
	count = 0 
	vowels_y = 'aeiouy'
	for word in lst:
		if uses_all(word, vowels_y):
			count += 1
	return count




##############################################################################
def main():
    
    print(uses_all("hello", "eo"))
    print(uses_all_vowels(['aeioussss', 'hellp']))

if __name__ == '__main__':
    main()
