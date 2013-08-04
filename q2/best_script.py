from collections import Counter

numbers_file = open("numbers.txt")
numbers_list = [x.strip() for x in numbers_file.readlines()]

output_file = open("run_result.txt", "w")

result_list = []

for (a, b) in [(x, y) for (x, y) in Counter(numbers_list).most_common(len(set(numbers_list))) if y != 1]:
	result_list.append('"%s", %d\n' % (str(a), b))

output_file.writelines(result_list)
output_file.close()
numbers_file.close()
