
def find_letter(letter):
	with open('roster.txt', 'r') as f:
		data = f.read()
		list_of_all = data.split()
		name_lists = list_of_all[0::2]
	
	count = 0
	name_with_e = []
	for item in name_lists:
		if 'e' in item:
			count += 1
			# print(item)
			name_with_e.append(item)

	print(count)

	print(name_with_e)


	newfile = open('newfile.txt', 'w')
	for name in name_with_e:
		newfile.write(name + '\n')
	newfile.write(str(count))

def main():

	find_letter('e')
if __name__ == '__main__':
	main()




