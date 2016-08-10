




def find_letter(letter):
	with open('roster.txt', 'r') as f:
		data = f.read()
		list_of_all = data.split()
		name_lists = list_of_all[0::2]
	
	count = 0
	for item in name_lists:
		if 'e' in item:
			count += 1
			print(item)

	print(count)

				


def main():



	print(find_letter('e'))

			






if __name__ == '__main__':
	main()