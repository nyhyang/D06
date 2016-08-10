#!/usr/bin/env python3
# HW06_ch09_ex05.py

# (1)
# Write a function called is_abecedarian that returns True if the letters in a
# word appear in alphabetical order (double letters are ok).
#   - write is_abecedarian
# (2)
# How many abecedarian words are there?
#   - write additional function(s) to assist you
#   - number of abecedarian words:
##############################################################################
# Imports

# Body

def is_abecedarian(word):
	previous_letter = word[0]
	for letter in word:
		if letter < previous:
			return False
		previous = letter 
	return True

def cal_abecedarian(wordlst):
	with open('words.txt', 'r') as f:
		word_lists = f.read().strip()
	
	total_count = 0
	for word in wordlst:
		if is_abecedarian(word):
			total_count += 1
	return total_count


##############################################################################
def main():
    cal_abecedarian(word_lists)

if __name__ == '__main__':
    main()
