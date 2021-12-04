
def read_input(filename):
	with open(filename, "r") as f:
		return [int(x) for x in f.readlines()]

def part_1(data):
	return sum([1 if b > a else 0 for a, b in zip(data[:-1], data[1:])])

def generate(data):
	for i in range(0, len(data) - 2):
		yield sum(data[i:i + 3])

def part_2(data):
	return sum([1 if b > a else 0 for a, b in zip(generate(data[:-1]), generate(data[1:]))])

if __name__ == "__main__":
	test = read_input("test")
	data = read_input("input")

	test_out_1 = 7
	test_out_2 = 5

	print(f"Test 1: {part_1(test)} | {test_out_1}")
	print(f"Part 1: {part_1(data)}")
	print("-----------------------")
	print(f"Test 2: {part_2(test)} | {test_out_2}")
	print(f"Part 2: {part_2(data)}")
