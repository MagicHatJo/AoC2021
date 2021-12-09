from collections import defaultdict
from functools import reduce

class Display:

	def __init__(self, raw_input, raw_output):
		self.input = raw_input.split()
		self.output = raw_output[:-1].split()
		self.nums = self.decode()
		self.value = self.get_value()
	
	def decode(self):
		table = defaultdict(list)
		for digit in self.input + self.output:
			table[len(digit)].append(digit)
		
		nums = {}

		if table[2]: nums[frozenset(table[2][0])] = 1
		if table[3]: nums[frozenset(table[3][0])] = 7
		if table[4]: nums[frozenset(table[4][0])] = 4
		if table[7]: nums[frozenset(table[7][0])] = 8
		
		for digit in table[6]:
			if 4 in table and frozenset(table[4][0]).issubset(digit):
				nums[frozenset(digit)] = 9
			elif 7 in table and frozenset(table[3][0]).issubset(digit):
				nums[frozenset(digit)] = 0
			else:
				nums[frozenset(digit)] = 6
				nums[6] = frozenset(digit)

		for digit in table[5]:
			if 7 in table and frozenset(table[3][0]).issubset(digit):
				nums[frozenset(digit)] = 3
			elif 6 in table and frozenset(digit).issubset(nums[6]):
				nums[frozenset(digit)] = 5
			else:
				nums[frozenset(digit)] = 2
		
		return nums
	
	def get_value(self):
		num = 0
		for digit in self.output:
			num = num * 10 + self.nums[frozenset(digit)]
		return num

def read_input(filename):
	with open(filename, "r") as f:
		return [Display(*line.split('|')) for line in f.readlines()]

def part_1(data):
	return sum([sum([len(digit) in [2, 3, 4, 7] for digit in display.output]) for display in data])

def part_2(data):
	return sum([display.value for display in data])

if __name__ == "__main__":
	test = read_input("test")
	data = read_input("input")

	test_out_1 = 26
	test_out_2 = 61229

	print(f"Test 1: {part_1(test)} | {test_out_1}")
	print(f"Part 1: {part_1(data)}")
	print("-----------------------")
	print(f"Test 2: {part_2(test)} | {test_out_2}")
	print(f"Part 2: {part_2(data)}")