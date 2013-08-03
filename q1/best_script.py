numbers_file = open("numbers.txt");
numbers_list = sorted([int(x) for x in (numbers_file.readlines())])

output_file = open("run_result.txt", "w")

for i in range(len(numbers_list)):
	if i != (len(numbers_list) - 1):
		if (numbers_list[i + 1] != (numbers_list[i] + 1)):
			for j in range(1, (numbers_list[i + 1] - numbers_list[i])):
				miss_number = numbers_list[i] + j;
				if 0 <= miss_number <= 9:
					output_file.write('000%d\n' % (miss_number))
				elif 10 <= miss_number <= 99:
					output_file.write('00%d\n' % (miss_number))
				elif 100 <= miss_number <= 999:
					output_file.write('0%d\n' % (miss_number))
				else:
					output_file.write('%d\n' % (miss_number))
			
numbers_file.close()
output_file.close()
			
