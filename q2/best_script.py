from collections import Counter

numbers_file = open("numbers.txt")
numbers_list = numbers_file.readlines()#[x for x in ()]

output_file = open("run_result.txt", "w")

for (a, b) in [(x, y) for (x, y) in Counter(numbers_list).most_common(len(set(numbers_list))) if y != 1]:
	output_file.write('\"%s\", %d\n' % (str(a), b))
