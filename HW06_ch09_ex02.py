#!/usr/bin/env python3
# HW06_ch09_ex02.py

# (1)
# Write a function called has_no_e that returns True if the given word doesn't
# have the letter "e" in it.
#   - write has_no_e
# (2)
# Modify your program from 9.1 to print only the words that have no "e" and
# compute the percentage of the words in the list have no "e."
#   - print each approved word on new line, followed at the end by the %
#   - name your function print_no_e
##############################################################################
# Imports

# Body

def has_no_e(word):
	for letter in word:
		if "e" in letter:
			return False
		else:
			return True


def print_no_e(wordlists):
	list_length = len(wordlists)

	count = 0
	with_no_elist = []
	for words in wordlists:
		if 'e' in words:
			count += 1
			with_no_elist.append(words)
			percent = (1 - (count / list_length)) * 100
			
	print(with_no_elist)
	print("There is {} percent of the word that has no e".format(percent))






##############################################################################
def main():
	

    # has_no_e("hello")
    print_no_e(['aloha', 'hello', 'yell'])

if __name__ == '__main__':
    main()
