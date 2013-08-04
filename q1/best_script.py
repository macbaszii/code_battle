numbers_file = open("numbers.txt");
numbers_list = sorted([int(x) for x in (numbers_file.readlines())])

output_file = open("run_result.txt", "w")
missing_numbers = []

for i in range(len(numbers_list)):
	if i != (len(numbers_list) - 1):
		if (numbers_list[i + 1] != (numbers_list[i] + 1)):
			for j in range(1, (numbers_list[i + 1] - numbers_list[i])):
				miss_number = numbers_list[i] + j;
				if 0 <= miss_number <= 9:
				    missing_numbers.append('000%d\n' % (miss_number))
				elif 10 <= miss_number <= 99:
				    missing_numbers.append('00%d\n' % (miss_number))
				elif 100 <= miss_number <= 999:
				    missing_numbers.append('0%d\n' % (miss_number))
				else:
				    missing_numbers.append('%d\n' % (miss_number))

output_file.writelines(missing_numbers)
numbers_file.close()
output_file.close()
			
